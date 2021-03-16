import jsonpickle
from enum import Enum

class MsgType(Enum):
    CONNECT    = 1
    TEXT       = 2
    DISCONNECT = 3

class Message:
    def __init__(self, msgType, msg=''):
        self.msgType = msgType
        self.msg = msg

    def toJSON(self):
        return jsonpickle.encode(self)
