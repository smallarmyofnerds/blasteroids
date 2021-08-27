class PlayerInputs:
    def __init__(self):
        self.left = False
        self.right = False
        self.up = False
        self.fire = False

    def __repr__(self) -> str:
        return f"{self.left} {self.right} {self.up} {self.fire}"

    def is_anything_pressed(self):
        return self.left or self.right or self.up or self.fire
