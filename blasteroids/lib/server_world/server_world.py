class ServerWorld:
    def __init__(self, objects, my_ship_id):
        self.my_ship = None
        self.objects = objects
        self.objects_by_id = {}

        for object in objects:
            if object.id == my_ship_id:
                self.my_ship = object
            else:
                self.objects_by_id[object.id] = object
