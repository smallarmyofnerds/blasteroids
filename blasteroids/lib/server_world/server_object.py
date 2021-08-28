class ServerObject:
    def __init__(self, type, id, position, orientation, name):
        self.type = type
        self.id = id
        self.position = position
        self.orientation = orientation
        self.name = name

    def __repr__(self):
        return f'{self.type} id={self.id} position={self.position} orientation={self.orientation} name={self.name}'
