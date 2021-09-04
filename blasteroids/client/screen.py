from blasteroids.lib.constants import DOUBLE_FIRE_PICKUP_ID, DOUBLE_FIRE_WEAPON_ID, LASER_WEAPON_ID, PROXIMITY_MINE_PICKUP_ID, PROXIMITY_MINE_WEAPON_ID, RAPID_FIRE_PICKUP_ID, RAPID_FIRE_WEAPON_ID, ROCKET_PICKUP_ID, ROCKET_SALVO_PICKUP_ID, ROCKET_SALVO_WEAPON_ID, ROCKET_WEAPON_ID, SPREAD_FIRE_PICKUP_ID, SPREAD_FIRE_WEAPON_ID, TIME_BOMB_PICKUP_ID, TIME_BOMB_WEAPON_ID
import pygame
from pygame.math import Vector2
from pygame.transform import rotozoom

UP = Vector2(0, 1)


class Screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.world_width = 1000
        self.world_height = 1000
        self.surface = None
        self.camera_position = Vector2(0, 0)
        self.screen_bottom_left = Vector2(0, 0)
        self.font = pygame.font.Font(None, 32)

    def init(self):
        self.surface = pygame.display.set_mode(size=(self.width, self.height), flags=pygame.RESIZABLE)

    def set_window_size(self, width, height):
        self.width = width
        self.height = height

    def initialize_world(self, world_width, world_height):
        self.world_width = world_width
        self.world_height = world_height

    def reset(self):
        self.surface.fill((0, 0, 0))
        for i in range(int((self.world_width + 1) / 500)):
            pygame.draw.line(self.surface, (255, 255, 255), self._world_to_viewport(Vector2(i * 500, self.world_height)), self._world_to_viewport(Vector2(i * 500, 0)))
        for i in range(int((self.world_height + 1) / 500)):
            pygame.draw.line(self.surface, (255, 255, 255), self._world_to_viewport(Vector2(0, i * 500)), self._world_to_viewport(Vector2(self.world_width, i * 500)))

    def move_camera_to(self, position):
        self.camera_position = position
        self.screen_bottom_left.x = position.x - 0.5 * self.width
        self.screen_bottom_left.y = position.y - 0.5 * self.height

    def _world_to_viewport(self, position):
        viewport_position = position - self.screen_bottom_left
        viewport_position.y = self.height - viewport_position.y
        return viewport_position

    def draw_sprite(self, sprite, position, orientation):
        angle = orientation.angle_to(UP)
        rotated_sprite = rotozoom(sprite, -1 * angle, 1.0)
        rotated_sprite_rect = rotated_sprite.get_rect()
        rotated_sprite_rect.center = self._world_to_viewport(position)
        self.surface.blit(rotated_sprite, rotated_sprite_rect)

    def pickup_id_from_weapon_id(self, active_weapon_id):
        return {
            LASER_WEAPON_ID: None,
            DOUBLE_FIRE_WEAPON_ID: DOUBLE_FIRE_PICKUP_ID,
            SPREAD_FIRE_WEAPON_ID: SPREAD_FIRE_PICKUP_ID,
            RAPID_FIRE_WEAPON_ID: RAPID_FIRE_PICKUP_ID,
            ROCKET_WEAPON_ID: ROCKET_PICKUP_ID,
            ROCKET_SALVO_WEAPON_ID: ROCKET_SALVO_PICKUP_ID,
            TIME_BOMB_WEAPON_ID: TIME_BOMB_PICKUP_ID,
            PROXIMITY_MINE_WEAPON_ID: PROXIMITY_MINE_PICKUP_ID,
        }[active_weapon_id]

    def draw_ui(self, health, shield, active_weapon_id, sprite_library):
        self.health_message = self.font.render(str(health), True, (0, 255, 0))
        self.health_width = self.health_message.get_width()

        self.shield_message = self.font.render(str(shield), True, (0, 204, 255))
        self.shield_width = self.shield_message.get_width()

        self.surface.blit(self.health_message, (75 - int(self.health_width), 25, 100, 100))
        self.surface.blit(self.shield_message, (150 - int(self.shield_width), 25, 100, 100))

        if active_weapon_id:
            pickup_id = self.pickup_id_from_weapon_id(active_weapon_id)
            if pickup_id:
                self.surface.blit(sprite_library.pickup_sprites[pickup_id], (self.width - 75, 25, 50, 50))
