from .message_decoder import MessageDecoder
from .hello_message import HelloMessage

class HelloMessageDecoder(MessageDecoder):
    def decode(self, encoded_message):
        player_name = encoded_message.pop_string()
        return HelloMessage(player_name)
