class ServerConnection:
    def __init__(self):
        self.running = False

    def send_inputs(self, inputs):
        print(inputs)

    def start(self):
        self.running = True
        while self.running:
            pass

    def stop(self):
        self.running = False
