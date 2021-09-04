class Hud:
    def __init__(self, sprite_library):
        self.sprite_library = sprite_library
        self.health = 0
        self.shield = 0
        self.active_weapon_id = None

    def update(self, health, shield, active_weapon_id):
        self.health = health
        self.shield = shield
        self.active_weapon_id = active_weapon_id

    def draw(self, screen):
        screen.draw_ui(self.health, self.shield, self.active_weapon_id, self.sprite_library)
