class Hud:
    def __init__(self, sprite_library):
        self.sprite_library = sprite_library
        self.health = 0
        self.shield = 0
        self.active_weapon = ''

    def update(self, health, shield, active_weapon):
        self.health = health
        self.shield = shield
        self.active_weapon = active_weapon

    def draw(self, screen):
        screen.draw_ui(self.health, self.shield, self.active_weapon, self.sprite_library)
