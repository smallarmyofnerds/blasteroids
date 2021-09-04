from .server_orientable_object import ServerOrientableObject
from ..constants import SHIP_OBJECT_ID


class ServerShip(ServerOrientableObject):
    def __init__(self, object_id, position, orientation, ship_id, health, shield, active_weapon_id, is_engine_on):
        super(ServerShip, self).__init__(SHIP_OBJECT_ID, object_id, position, orientation)
        self.ship_id = ship_id
        self.health = health
        self.shield = shield
        self.active_weapon_id = active_weapon_id
        self.is_engine_on = is_engine_on

    def from_ship(ship):
        return ServerShip(ship.id, ship.position, ship.orientation, ship.player_id, ship.health, ship.shield, ship.get_active_weapon(), ship.is_engine_on)

    def encode(self, message_encoder):
        super(ServerShip, self).encode(message_encoder)
        message_encoder.push_byte(self.ship_id)
        message_encoder.push_short(self.health)
        message_encoder.push_short(self.shield)
        message_encoder.push_byte(self.active_weapon_id)
        message_encoder.push_boolean(self.is_engine_on)

    def decode_body(encoded_message):
        object_id, position, orientation = ServerOrientableObject.decode_body(encoded_message)
        ship_id = encoded_message.pop_byte()
        health = encoded_message.pop_short()
        shield = encoded_message.pop_short()
        active_weapon_id = encoded_message.pop_byte()
        is_engine_on = encoded_message.pop_boolean()
        return ServerShip(object_id, position, orientation, ship_id, health, shield, active_weapon_id, is_engine_on)
