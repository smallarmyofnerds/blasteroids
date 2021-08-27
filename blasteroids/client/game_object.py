class GameObject:
    def __init__(self, server_object):
        self.id = server_object.id
        self.position = server_object.position
        self.orientation = server_object.orientation
        self.name = server_object.name

    def _update(self, position, orientation):
        self.position = position
        self.orientation = orientation

    def destroy(self):
        pass

    def draw(self, screen):
        pass
