import configparser
import datetime
import hashlib
import logging
import mimetypes
import os
import re
import multiprocessing
import socket
import subprocess
import sys
import time as tm
import platform
import requests
import randomname

from .worker import Worker

INIT_MISSING = 'initialize a run using init() first'
QUEUE_SIZE = 5000

def get_cpu_info():
    """
    Get CPU info
    """
    model_name = ''
    arch = ''

    try:
        info = subprocess.check_output('lscpu').decode().strip()
        for line in info.split('\n'):
            if 'Model name' in line:
                model_name = line.split(':')[1].strip()
            if 'Architecture' in line:
                arch = line.split(':')[1].strip()
    except Exception:
        # TODO: Try /proc/cpuinfo
        pass

    return model_name, arch


def get_gpu_info():
    """
    Get GPU info
    """
    try:
        output = subprocess.check_output(["nvidia-smi",
                                          "--query-gpu=name,driver_version",
                                          "--format=csv"])
        lines = output.split(b'\n')
        tokens = lines[1].split(b', ')
    except Exception:
        return {'name': '', 'driver_version': ''}

    return {'name': tokens[0].decode(), 'driver_version': tokens[1].decode()}


def calculate_sha256(filename):
    """
    Calculate sha256 checksum of the specified file
    """
    sha256_hash = hashlib.sha256()
    try:
        with open(filename, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
            return sha256_hash.hexdigest()
    except Exception:
        pass

    return None


def validate_timestamp(timestamp):
    """
    Validate a user-provided timestamp
    """
    try:
        datetime.datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S.%f')
    except ValueError:
        return False

    return True


class Simvue(object):
    """
    Track simulation details based on token and URL
    """
    def __init__(self):
        self._name = None
        self._suppress_errors = False
        self._queue_blocking = False
        self._status = None
        self._upload_time_log = None
        self._upload_time_event = None
        self._data = []
        self._events = []
        self._step = 0
        self._metrics_queue = multiprocessing.Manager().Queue(maxsize=QUEUE_SIZE)
        self._events_queue = multiprocessing.Manager().Queue(maxsize=QUEUE_SIZE)

    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        if self._name:
            self.set_status('completed')

    def init(self, name=None, metadata={}, tags=[], description=None, folder='/'):
        """
        Initialise a run
        """
        # Try environment variables
        token = os.getenv('SIMVUE_TOKEN')
        self._url = os.getenv('SIMVUE_URL')

        if not token or not self._url:
            # Try config file
            try:
                config = configparser.ConfigParser()
                config.read('simvue.ini')
                token = config.get('server', 'token')
                self._url = config.get('server', 'url')
            except Exception:
                pass

        if not name:
            name = randomname.get_name()

        if not token or not self._url:
            raise RuntimeError('Unable to get URL and token from environment variables or config file')

        if not re.match(r'^[a-zA-Z0-9\-\_\s\/\.:]+$', name):
            raise RuntimeError('specified name is invalid')

        if not isinstance(tags, list):
            raise RuntimeError('tags must be a list')

        if not isinstance(metadata, dict):
            raise RuntimeError('metadata must be a dict')

        self._headers = {"Authorization": "Bearer %s" % token}
        self._name = name
        self._start_time = tm.time()

        self._worker = Worker(self._metrics_queue, self._events_queue, name, self._url, self._headers)

        data = {'name': name,
                'metadata': metadata,
                'tags': tags}

        if description:
            data['description'] = description

        cpu = get_cpu_info()
        gpu = get_gpu_info()

        data['system'] = {}
        data['system']['cwd'] = os.getcwd()
        data['system']['hostname'] = socket.gethostname()
        data['system']['pythonversion'] = '%d.%d.%d' % (sys.version_info.major,
                                                        sys.version_info.minor,
                                                        sys.version_info.micro)
        data['system']['platform'] = {}
        data['system']['platform']['system'] = platform.system()
        data['system']['platform']['release'] = platform.release()
        data['system']['platform']['version'] = platform.version()
        data['system']['cpu'] = {}
        data['system']['cpu']['arch'] = cpu[1]
        data['system']['cpu']['processor'] = cpu[0]
        data['system']['gpu'] = {}
        data['system']['gpu']['name'] = gpu['name']
        data['system']['gpu']['driver'] = gpu['driver_version']

        if not folder.startswith('/'):
            raise RuntimeError('the folder must begin with /')

        data['folder'] = folder

        try:
            response = requests.post('%s/api/runs' % self._url, headers=self._headers, json=data)
        except Exception:
            return False

        if response.status_code == 409:
            raise RuntimeError('Run with name %s already exists' % name)

        if response.status_code != 200:
            raise RuntimeError('Unable to create run due to: %s', response.text)

        if multiprocessing.current_process()._parent_pid is None:
            self._worker.start()

        return True

    def config(self, suppress_errors=False, queue_blocking=False):
        """
        Optional configuration
        """
        if not isinstance(suppress_errors, bool):
            raise RuntimeError('suppress_errors must be boolean')
        self._suppress_errors = suppress_errors

        if not isinstance(queue_blocking, bool):
            raise RuntimeError('queue_blocking must be boolean')
        self._queue_blocking = queue_blocking

    def update_metadata(self, metadata):
        """
        Add/update metadata
        """
        if not self._name:
            raise RuntimeError(INIT_MISSING)

        if not isinstance(metadata, dict):
            raise RuntimeError('metadata must be a dict')

        data = {'run': self._name, 'metadata': metadata}

        try:
            response = requests.put('%s/runs' % self._url, headers=self._headers, json=data)
        except Exception:
            return False

        if response.status_code == 200:
            return True

        return False

    def log_event(self, message, timestamp=None):
        """
        Write event
        """
        if not self._name:
            raise RuntimeError(INIT_MISSING)

        if self._status:
            raise RuntimeError('Cannot log events after run has ended')

        data = {}
        data['run'] = self._name
        data['message'] = message
        data['timestamp'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        if timestamp is not None:
            if validate_timestamp(timestamp):
                data['timestamp'] = timestamp
            else:
                raise RuntimeError('Invalid timestamp format')

        try:
            self._events_queue.put(data, block=self._queue_blocking)
        except multiprocessing.queue.Full:
            pass

        return True

    def log_metrics(self, metrics, time=None, timestamp=None):
        """
        Write metrics
        """
        if not self._name:
            raise RuntimeError(INIT_MISSING)

        if self._status:
            raise RuntimeError('Cannot log metrics after run has ended')

        if not isinstance(metrics, dict) and not self._suppress_errors:
            raise RuntimeError('Metrics must be a dict')

        data = {}
        data['run'] = self._name
        data['values'] = metrics
        data['time'] = tm.time() - self._start_time
        if time is not None:
            data['time'] = time
        data['timestamp'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        if timestamp is not None:
            if validate_timestamp(timestamp):
                data['timestamp'] = timestamp
            else:
                raise RuntimeError('Invalid timestamp format')
        data['step'] = self._step

        self._step += 1

        try:
            self._metrics_queue.put(data, block=self._queue_blocking)
        except multiprocessing.queue.Full:
            pass

        return True

    def save(self, filename, category, filetype=None):
        """
        Upload file
        """
        if not self._name:
            raise RuntimeError(INIT_MISSING)

        if not os.path.isfile(filename):
            raise RuntimeError('File %s does not exist' % filename)

        if filetype:
            mimetypes_valid = []
            mimetypes.init()
            for item in mimetypes.types_map:
                mimetypes_valid.append(mimetypes.types_map[item])

            if filetype not in mimetypes_valid:
                raise RuntimeError('Invalid MIME type specified')

        data = {}
        data['name'] = os.path.basename(filename)
        data['run'] = self._name
        data['category'] = category
        data['checksum'] = calculate_sha256(filename)
        data['size'] = os.path.getsize(filename)
        data['originalPath'] = os.path.abspath(os.path.expanduser(os.path.expandvars(filename)))

        # Determine mimetype
        if not filetype:
            mimetypes.init()
            mimetype = mimetypes.guess_type(filename)[0]
            if not mimetype:
                mimetype = 'application/octet-stream'
        else:
            mimetype = filetype

        data['type'] = mimetype

        # Get presigned URL
        try:
            resp = requests.post('%s/api/data' % self._url, headers=self._headers, json=data)
        except Exception:
            return False

        if 'url' in resp.json():
            # Upload file
            try:
                with open(filename, 'rb') as fh:
                    response = requests.put(resp.json()['url'], data=fh, timeout=30)
                    if response.status_code != 200:
                        return False
            except Exception:
                return False

        return True

    def set_status(self, status):
        """
        Set run status
        """
        if status not in ('completed', 'failed', 'terminated'):
            raise RuntimeError('invalid status')

        data = {'name': self._name, 'status': status}
        self._status = status

        try:
            response = requests.put('%s/api/runs' % self._url, headers=self._headers, json=data)
        except Exception:
            return False

        if response.status_code == 200:
            return True

        return False

    def close(self):
        """
        Close the run
        """
        self.set_status('completed')

    def set_folder_details(self, path, metadata={}, tags=[], description=None):
        """
        Add metadata to the specified folder
        """
        if not isinstance(metadata, dict):
            raise RuntimeError('metadata must be a dict')

        if not isinstance(tags, list):
            raise RuntimeError('tags must be a list')

        data = {'path': path}

        if metadata:
            data['metadata'] = metadata

        if tags:
            data['tags'] = tags

        if description:
            data['description'] = description

        try:
            response = requests.put('%s/api/folders' % self._url, headers=self._headers, json=data)
        except Exception:
            return False

        if response.status_code == 200:
            return True

        return False

    def add_alert(self, name, type, metric, frequency, window, threshold=None, range_low=None, range_high=None, notification='none'):
        """
        Creates an alert with the specified name (if it doesn't exist) and applies it to the current run
        """
        if type not in ('is below', 'is above', 'is outside range', 'is inside range'):
            raise RuntimeError('alert type invalid')

        if type in ('is below', 'is above') and threshold is None:
            raise RuntimeError('threshold must be defined for the specified alert type')

        if type in ('is outside range', 'is inside range') and (range_low is None or range_high is None):
            raise RuntimeError('range_low and range_high must be defined for the specified alert type')

        if notification not in ('none', 'email'):
            raise RuntimeError('notification must be either none or email')

        alert = {'name': name,
                 'type': type,
                 'metric': metric,
                 'frequency': frequency,
                 'window': window,
                 'notification': notification}

        if threshold is not None:
            alert['threshold'] = threshold
        elif range_low is not None and range_high is not None:
            alert['range_low'] = range_low
            alert['range_high'] = range_high

        try:
            response = requests.post('%s/api/alerts' % self._url, headers=self._headers, json=alert)
        except Exception:
            return False

        if response.status_code != 200 and response.status_code != 409:
            raise RuntimeError('unable to create alert')

        data = {'name': self._name, 'alert': name}

        try:
            response = requests.put('%s/api/runs' % self._url, headers=self._headers, json=data)
        except Exception:
            return False

        if response.status_code == 200:
            return True


class SimvueHandler(logging.Handler):
    """
    Class for handling logging to Simvue
    """
    def __init__(self, client):
        logging.Handler.__init__(self)
        self._client = client

    def emit(self, record):
        if 'simvue.' in record.name:
            return

        msg = self.format(record)

        try:
            self._client.log_event(msg)
        except Exception:
            logging.Handler.handleError(self, record)

    def flush(self):
        pass

    def close(self):
        pass
