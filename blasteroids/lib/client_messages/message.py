class Message:
    def __init__(self, type):
        self.type = type

    def dispatch(self, handler):
        raise Exception(f'dispatch() not implemented on {self.type}')

    def __repr__(self):
        return self.type
