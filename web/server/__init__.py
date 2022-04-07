import multiprocessing
import os


def get_env(key, default):
    return os.environ.get(key, default)


def _number_of_workers():
    return (multiprocessing.cpu_count() * 2) + 1


def default_build_path():
    return os.path.join(os.getcwd(), 'build')


DEFAULT_LISTEN_ADDRESS = get_env('LISTEN_ADDRESS', '0.0.0.0')
DEFAULT_LISTEN_PORT = get_env('LISTEN_ADDRESS', 5000)
DEFAULT_WORKERS_COUNT = get_env('LISTEN_ADDRESS', _number_of_workers())
DEFAULT_WORKER_TIMEOUT = get_env('LISTEN_ADDRESS', 60)
DEFAULT_STATIC_FOLDER = get_env('STATIC_FOLDER', default_build_path())
