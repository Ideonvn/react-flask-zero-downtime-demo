import os
import socket


class SystemInfo:

    info_called = 0

    def get_system_info(self):
        self.info_called = self.info_called + 1
        return {
            'hostname': f'{socket.gethostname()}_new2',
            'called': self.info_called,
            'pid': os.getpid(),
        }
