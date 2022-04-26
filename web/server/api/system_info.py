import os
import socket
import logging

from server import db

LOGGER = logging.getLogger(__name__)

class SystemInfoModal(db.Model):
    __tablename__ = "system_info"

    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String)
    called = db.Column(db.Integer)
    pid = db.Column(db.Integer)

    @property
    def serialized(self):
        """Return object data in serializeable format"""
        data = {
            "id": self.id,
            "hostname": self.hostname,
            "called": self.called,
            "pid": self.pid,
        }
        return data

class SystemInfo:

    def __init__(self) -> None:
        db.create_all()

    def get_system_info(self):
        hostname = f'{socket.gethostname()}_new',
        pid = os.getpid()

        system_info = db.session.query(SystemInfoModal).filter_by(
            hostname=hostname, pid=pid).one_or_none()

        if system_info:
            system_info.called += 1
        else:
           system_info = SystemInfoModal(
               hostname=hostname,
               called=1,
               pid=pid
           )
           db.session.add(system_info)

        db.session.commit()

        LOGGER.info(system_info.serialized)
        return system_info.serialized
