class GameObject:
    def __init__(self, id, position, orientation):
        self.id = id
        self.position = position
        self.orientation = orientation

    def _update(self, position, orientation):
        self.position = position
        self.orientation = orientation

    def destroy(self):
        pass

    def draw(self, screen):
        pass
