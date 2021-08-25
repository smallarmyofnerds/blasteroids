import threading


class SynchronizedList:
    def __init__(self):
        self.items = []
        self.lock = threading.Lock()

    def append(self, item):
        self.lock.acquire()
        self.items.append(item)
        self.lock.release()

    def remove(self, item):
        self.lock.acquire()
        self.items.remove(item)
        self.lock.release()
