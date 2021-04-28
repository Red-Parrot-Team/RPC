from enum import Enum

class ConfirmType(Enum):
    REGISTRATION    = 0
    NOTCONFIRM      = 1
    CONFIRMING      = 2
    CONFIRM         = 3  

class State:
    def __init__(self):
        self.confirm_type = ConfirmType.REGISTRATION
    
    def isNotConfirm(self):
        if self.confirm_type == ConfirmType.NOTCONFIRM:
            return True
        return False

    def isConfirming(self):
        if self.confirm_type == ConfirmType.CONFIRMING:
            return True
        return False