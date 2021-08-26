import threading
from collections import deque

class SynchronizedQueue:
    def __init__(self):
        self.items = deque([])
        self.lock = threading.Lock()

    def push(self, item):
        self.lock.acquire()
        self.items.append(item)
        self.lock.release()
    
    def pop(self):
        self.lock.acquire()
        item = self.items.popleft()
        self.lock.release()
        return item
    
    def is_empty(self):
        self.lock.acquire()
        is_empty = len(self.items) == 0
        self.lock.release()
        return is_empty
    