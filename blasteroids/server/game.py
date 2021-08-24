import threading

class Game(threading.Thread):
    def __init__(self):
        self.client_connections = []
        self.client_connections_lock = threading.Lock()
    
    def add_client_connection(self, client_connection):
        self.client_connections_lock.acquire()
        self.client_connections.append(client_connection)
        self.client_connections_lock.release()

    def run(self):
        pass
