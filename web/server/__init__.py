import logging.config
import multiprocessing
import os

import yaml
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


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

app = Flask(__name__, static_folder=DEFAULT_STATIC_FOLDER, static_url_path='/')
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://test_user:test_pwd@db/test_db"

db = SQLAlchemy(app)


def _load_yaml():
    with open('logging.conf', 'r') as stream:
        return yaml.safe_load(stream)


logging.config.dictConfig(_load_yaml())
