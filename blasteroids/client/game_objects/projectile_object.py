from .orientable_game_object import OrientableGameObject


class ProjectileObject(OrientableGameObject):
    def __init__(self, server_projectile, sprite_library):
        super(ProjectileObject, self).__init__(server_projectile)
        self.sprite = sprite_library.projectile_sprites[server_projectile.projectile_id]

    def draw(self, screen, my_position):
        screen.draw_sprite(self.sprite, self.position, self.orientation)

    def update(self, server_projectile):
        super(ProjectileObject, self).update(server_projectile)
