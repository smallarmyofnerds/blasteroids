from .message import Message
from .message_encoder import MessageEncoder


class ReadyMessage(Message):
    TYPE = 'REDY'

    def __init__(self):
        super(ReadyMessage, self).__init__(ReadyMessage.TYPE)

    def __repr__(self):
        return f'{super(ReadyMessage, self).__repr__()}'


class ReadyMessageEncoder(MessageEncoder):
    def __init__(self):
        super(ReadyMessageEncoder, self).__init__(ReadyMessage.TYPE)

    def encode(self, message):
        return super(ReadyMessageEncoder, self)._encode_type()

    def decode(self, encoded_message):
        return ReadyMessage()
