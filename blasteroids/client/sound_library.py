from blasteroids.lib.constants import (
    ARMING_NOISE_SOUND_ID, BOMB_CLANK_SOUND_ID, BOMB_EXPLOSION_SOUND_ID, DOUBLE_FIRE_PICKUP_SOUND_ID, DOUBLE_FIRE_SHOT_SOUND_ID,
    HEALING_PICKUP_SOUND_ID, IMPACT_SOUND_ID, LASER_HIT_SOUND_ID, LASER_SOUND_ID, MEGA_PICKUP_SOUND_ID, PROXIMITY_MINE_PICKUP_SOUND_ID,
    PROXIMITY_MINE_SHOT_SOUND_ID, RAPID_FIRE_PICKUP_SOUND_ID, ROCKET_EXPLOSION_SOUND_ID, ROCKET_PICKUP_SOUND_ID,
    ROCKET_SALVO_EXPLOSION_SOUND_ID, ROCKET_SALVO_PICKUP_SOUND_ID, ROCKET_SALVO_SHOT_SOUND_ID, ROCKET_SHOT_SOUND_ID,
    SHIELDING_PICKUP_SOUND_ID, SHIP_IMPACT_SOUND_ID, SPREAD_FIRE_PICKUP_SOUND_ID, SPREAD_FIRE_SHOT_SOUND_ID, TIME_BOMB_PICKUP_SOUND_ID,
    TIME_BOMB_SHOT_SOUND_ID, SHIP_ENGINE_SOUND_ID, RAPID_FIRE_SHOT_SOUND_ID, ROCKET_EXHAUST_SOUND_ID
)
import pygame
from pygame.mixer import Sound


class SoundLibrary:
    def __init__(self):
        self.sounds = {}
        pygame.mixer.init()
        pygame.mixer.set_num_channels(32)

        self.sounds[LASER_SOUND_ID] = Sound('assets/sounds/laser.wav')
        self.sounds[IMPACT_SOUND_ID] = Sound('assets/sounds/impact.wav')
        self.sounds[SHIP_IMPACT_SOUND_ID] = Sound('assets/sounds/shipimpact.wav')
        self.sounds[HEALING_PICKUP_SOUND_ID] = Sound('assets/sounds/healing_pickup.wav')
        self.sounds[SHIELDING_PICKUP_SOUND_ID] = Sound('assets/sounds/shielding_pickup.wav')
        self.sounds[RAPID_FIRE_PICKUP_SOUND_ID] = Sound('assets/sounds/rapid_fire_pickup.wav')
        self.sounds[SPREAD_FIRE_PICKUP_SOUND_ID] = Sound('assets/sounds/spread_fire_pickup.wav')
        self.sounds[DOUBLE_FIRE_PICKUP_SOUND_ID] = Sound('assets/sounds/double_fire_pickup.wav')
        self.sounds[ROCKET_PICKUP_SOUND_ID] = Sound('assets/sounds/rocket_pickup.wav')
        self.sounds[ROCKET_SALVO_PICKUP_SOUND_ID] = Sound('assets/sounds/rocket_salvo_pickup.wav')
        self.sounds[TIME_BOMB_PICKUP_SOUND_ID] = Sound('assets/sounds/time_bomb_pickup.wav')
        self.sounds[PROXIMITY_MINE_PICKUP_SOUND_ID] = Sound('assets/sounds/proximity_mine_pickup.wav')
        self.sounds[MEGA_PICKUP_SOUND_ID] = Sound('assets/sounds/mega_pickup.wav')
        self.sounds[ROCKET_SHOT_SOUND_ID] = Sound('assets/sounds/rocket_shot.wav')
        self.sounds[TIME_BOMB_SHOT_SOUND_ID] = Sound('assets/sounds/bomb_shot.wav')
        self.sounds[PROXIMITY_MINE_SHOT_SOUND_ID] = Sound('assets/sounds/bomb_shot.wav')
        self.sounds[ROCKET_SALVO_SHOT_SOUND_ID] = Sound('assets/sounds/rocket_salvo_shot.wav')
        self.sounds[ROCKET_EXPLOSION_SOUND_ID] = Sound('assets/sounds/rocket_explosion.wav')
        self.sounds[ROCKET_SALVO_EXPLOSION_SOUND_ID] = Sound('assets/sounds/rocket_salvo_explosion.wav')
        self.sounds[BOMB_EXPLOSION_SOUND_ID] = Sound('assets/sounds/bomb_explosion.wav')
        self.sounds[SPREAD_FIRE_SHOT_SOUND_ID] = Sound('assets/sounds/spread_fire_shot.wav')
        self.sounds[DOUBLE_FIRE_SHOT_SOUND_ID] = Sound('assets/sounds/double_fire_shot.wav')
        self.sounds[ARMING_NOISE_SOUND_ID] = Sound('assets/sounds/arming_noise.wav')
        self.sounds[BOMB_CLANK_SOUND_ID] = Sound('assets/sounds/bomb_clank.wav')
        self.sounds[LASER_HIT_SOUND_ID] = Sound('assets/sounds/laser_hitting_ship.wav')

        self.sounds[SHIP_ENGINE_SOUND_ID] = Sound('assets/sounds/ship_engine.wav')
        self.sounds[RAPID_FIRE_SHOT_SOUND_ID] = Sound('assets/sounds/rapid_fire_shot.wav')
        self.sounds[ROCKET_EXHAUST_SOUND_ID] = Sound('assets/sounds/rocket_exhaust.wav')
