from .message import Message
from .message_encoder import MessageEncoder


class EntryMessage(Message):
    TYPE = 'ENTR'

    def __init__(self, player_list):
        super(EntryMessage, self).__init__(EntryMessage.TYPE)
        self.player_list = player_list

    def dispatch(self, handler):
        return handler.handle_ENTR(self)

    def __repr__(self):
        return f"{super(EntryMessage, self).__repr__()}:{','.join(self.player_list)}"


class EntryMessageEncoder(MessageEncoder):
    def __init__(self):
        super(EntryMessageEncoder, self).__init__(EntryMessage.TYPE)

    def encode(self, message):
        return super(EntryMessageEncoder, self)._encode_type() + self._encode_string_array(message.player_list)

    def decode(self, encoded_message):
        player_list = encoded_message.pop_string_array()
        return EntryMessage(player_list)
