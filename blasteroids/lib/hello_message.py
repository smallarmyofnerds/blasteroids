from .message import Message

class HelloMessage(Message):
    TYPE = 'HELO'

    def __init__(self, player_name):
        super(HelloMessage, self).__init__(HelloMessage.TYPE)
        self.player_name = player_name

    def encode(self):
        return super(HelloMessage, self).encode() + self.encode_string(self.player_name)
    
    def __repr__(self):
        return f'{super(HelloMessage, self).__repr__()}:{self.player_name}'
