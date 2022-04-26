import logging

import gunicorn.app.base

from server import (DEFAULT_LISTEN_ADDRESS, DEFAULT_LISTEN_PORT,
                    DEFAULT_WORKER_TIMEOUT, DEFAULT_WORKERS_COUNT, app)
from server.api import SystemInfo

system_info = SystemInfo()

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/health')
def health():
    return {'up': True}


@app.route('/info')
def get_current_info():
    return system_info.get_system_info()


class GunicornApplication(gunicorn.app.base.BaseApplication):

    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):
        config = {key: value for key, value in self.options.items()
                  if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


if __name__ == '__main__':
    options = {
        'bind': '%s:%s' % (DEFAULT_LISTEN_ADDRESS, DEFAULT_LISTEN_PORT),
        'workers': DEFAULT_WORKERS_COUNT,
        'timeout': DEFAULT_WORKER_TIMEOUT,
        'reload': True,
    }
    # time.sleep(10)
    GunicornApplication(app, options).run()
