class ServerWorld:
    def __init__(self, objects, my_ship_id, health, shield, active_weapon, is_engine_on):
        self.my_ship = None
        self.objects = []
        self.objects_by_id = {}
        self.health = health
        self.shield = shield
        self.active_weapon = active_weapon
        self.is_engine_on = is_engine_on

        for object in objects:
            if object.id == my_ship_id:
                self.my_ship = object
            else:
                self.objects.append(object)
                self.objects_by_id[object.id] = object

    def __repr__(self):
        s = '-----\n'
        s += f'my_ship: {self.my_ship}\n'
        for object in self.objects:
            s += str(object) + '\n'
        s += '-----'
        return s
