class GameObject:
    def __init__(self, server_object):
        self.type_id = server_object.type_id
        self.object_id = server_object.object_id
        self.position = server_object.position

    def update(self, server_object):
        self.position = server_object.position

    def draw(self, screen, my_position):
        pass
