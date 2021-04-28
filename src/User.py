class User:
    def __init__(self, nickname):
        self.nickname = nickname
    
    def isRegistrated(self):
        if self.nickname:
            return True
        return False