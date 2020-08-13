class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else: 
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:
    def __init__(self):
        self.rooms = {}
    
    # this will be the key in the rooms dictionary
    def add_room(self, room_id):
        self.rooms[room_id] = set()
    
    # these will be the connections/directions
    def add_edge(self, v1, v2, v3, v4):
        pass

    def get_neighbors(self, room_id):
        return self.rooms[room_id]