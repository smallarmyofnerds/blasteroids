import random
from .game_objects.time_bomb_pickup import TimeBombPickup
from .game_objects.proximity_mine_pickup import ProximityMinePickup
from .game_objects.mega_shield_pickup import MegaShieldPickup
from .game_objects.rocket_pickup import RocketPickup
from .game_objects.rocket_salvo_pickup import RocketSalvoPickup
from .game_objects.spread_fire_pickup import SpreadFirePickup
from .game_objects.double_fire_pickup import DoubleFirePickup
from .game_objects.mega_heart_pickup import MegaHeartPickup
from .game_objects.heart_pickup import HeartPickup
from .game_objects.shield_pickup import ShieldPickup
from .game_objects.rapid_fire_pickup import RapidFirePickup


class DropTable:
    def __init__(self, chance, drops):
        self.chance = chance
        self.drops = drops


class LootFactory:
    def __init__(self, config, id_generator):
        self.config = config
        self.id_generator = id_generator
        self.random_drops = {
            3: DropTable(config.loot.level_3_chance, config.loot.level_3_drops),
            2: DropTable(config.loot.level_2_chance, config.loot.level_2_drops),
            1: DropTable(config.loot.level_1_chance, config.loot.level_1_drops),
        }
    
    def create(self, level, position):
        drop_table = self.random_drops[level]
        roll = 100 * random.random()
        if roll <= drop_table.chance:
            return self._create(random.choice(drop_table.drops), position)
        return None

    def _create(self, name, position):
        if name == 'heart':
            return HeartPickup(self.id_generator.get_next_id(), position, self.config.heart.health_amount, self.config.heart.pickup_lifespan)
        elif name == 'mega_heart':
            return MegaHeartPickup(self.id_generator.get_next_id(), position, self.config.mega_heart.pickup_lifespan)
        elif name == 'shield':
            return ShieldPickup(self.id_generator.get_next_id(), position, self.config.shield.shield_amount, self.config.shield.pickup_lifespan)
        elif name == 'mega_shield':
            return MegaShieldPickup(self.id_generator.get_next_id(), position, self.config.mega_shield.pickup_lifespan)
        elif name == 'double_fire':
            return DoubleFirePickup(self.id_generator.get_next_id(), position, self.config.double_fire.pickup_lifespan)
        elif name == 'spread_fire':
            return SpreadFirePickup(self.id_generator.get_next_id(), position, self.config.spread_fire.pickup_lifespan)
        elif name == 'rapid_fire':
            return RapidFirePickup(self.id_generator.get_next_id(), position, self.config.rapid_fire.pickup_lifespan)
        elif name == 'rocket':
            return RocketPickup(self.id_generator.get_next_id(), position, self.config.rocket.pickup_lifespan)
        elif name == 'rocket_salvo':
            return RocketSalvoPickup(self.id_generator.get_next_id(), position, self.config.rocket_salvo.pickup_lifespan)
        elif name == 'proximity_mine':
            return ProximityMinePickup(self.id_generator.get_next_id(), position, self.config.proximity_mine.pickup_lifespan)
        elif name == 'time_bomb':
            return TimeBombPickup(self.id_generator.get_next_id(), position, self.config.time_bomb.pickup_lifespan)
        else:
            raise Exception('Unrecognized loot type')
