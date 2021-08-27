class PlayerInputState:
    def __init__(self):
        self.left = False
        self.right = False
        self.up = False
        self.fire = False

    def set_state(self, left, right, up, fire):
        self.left = left
        self.right = right
        self.up = up
        self.fire = fire
