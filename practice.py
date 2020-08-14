from room import Room
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

class Graph():
    def __init__(self):
        self.rooms = {}
        self.path = []
    
    # this will be the key in the rooms dictionary
    def add_room(self, room_id):
        self.rooms[room_id] = set()
    
    # these will be the connections/directions
    def add_edge(self, ):
        pass

    def get_neighbors(self, room_id):
        return self.rooms[room_id]
    
    def dft(self, starting_room):
        s = Stack()
        s.push(starting_room)

        while s.size() > 0:
            r = s.pop()
            print(f'rrrrrrrr: {r}')

            neighbors = self.get_neighbors(starting_room)
            print(f'NEIGHBORS: {neighbors}')
                    

                # for next_room in self.get_neighbors(r):
                #     s.push(next_room)
        return self.path

-----------------""" VERSION 2 """--------------------------
# Should I fill in the dict with the rooms as I go along?
# 

-----------------""" VERSION 2 """--------------------------
# How can I move? --> player.travel(direction) --> direction needs to be a string 'n', 's', 'e', or 'w'
# How can I pick a random path? --> DFT

""" PASSES TEST 1 """
# rooms = dict()
# visited = list()
# curr = player.current_room.id

# populate graph
# for i in range(0, len(world.rooms)):
#     rooms[i] = dict()

#     for exit in world.rooms[i].get_exits():
#         # print(f"TEST TEST TEST: {world.rooms[i].n_to.id}")
#         # print(f"ANOTHER TEST: {world.rooms[i].get_exits_id(exit)}")
#         room_num = world.rooms[i].get_exits_id(exit)
#         rooms[i].update({exit: room_num})
        
# print(f'GRAPH ROOMS: {rooms}')

# print(f'CURRENT_ROOM: {player.current_room.get_exits()}')

# def dft(starting_room):
#     s = Stack()
#     s.push(starting_room)    

#     while s.size() > 0 and len(visited) < len(rooms):
#         r = s.pop()
#         # print(f"rrrrrr {r}")
#         print(f"CURR: {r}")
#         if r not in visited:
#             visited.append(r)
#         neighbors = rooms[r]
#         # print(f'neighbors: {neighbors}')

#         for neighbor, value in neighbors.items():
#             if value not in visited:
#                 traversal_path.append(neighbor)
#                 s.push(value)
#     print(f'PATH: {traversal_path}')

# print(f"TRAVERSAL: {traversal_path}")
# dft(curr)

-----------------""" VERSION 1 """--------------------------
# NOTES:
""" Anything in yellow like this is original sprint code """
# Everything else commented out is made up of my notes.

# Loads the map into a dictionary --> reads from the different maps above and creates the 'text' for the map to generate
# prints out a dictionary of the rooms 
# value == a list of a tuple and a dictionary of directions
# What is in the tuple? 
# Ex --> 0: [(3,5), {'n': 1, 's': 5, 'e': 3, 'w': 7}]
# tuple represents (row, col) --> (row 3, col 5)
# room_graph --> list
""" room_graph=literal_eval(open(map_file, "r").read()) """

# print(f"LOOK HERE: \n\n {room_graph}, \n\n LEN OF ROOM_GRAPH: {len(room_graph)}")
# loads the rooms onto a graph
""" world.load_graph(room_graph) """
# print(f'\n\n \t\t ROOMS[0][0]: {world.rooms[0]}, STARTING ROOM: {world.starting_room}')
# print(f'\n\n \t\t LOADED WORLD OUTPUT: {world.rooms}') # --> output below can search for not None
# LOADED WORLD OUTPUT: [[None, None, None, None, None, None, None, None], [None, None, None, None, None, <room.Room object at 0x1056faf50>, None, None], [None, None, None, None, None, <room.Room object at 0x1056faf10>, None, None], [None, None, None, <room.Room object at 0x1056fadd0>, <room.Room object at 0x1056fad10>, <room.Room object at 0x1056fa510>, <room.Room object at 0x1056fa9d0>, <room.Room object at 0x1056faad0>], [None, None, None, None, None, <room.Room object at 0x1056fac90>, None, None], [None, None, None, None, None, <room.Room object at 0x1056fab50>, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None]]

# starting_room comes from world class 
# initialized as None, but after loading the rooms, is 000
# comes form world class self.rooms, initialized as an empty class that 
# is populated in def load_graph
"""player = Player(world.starting_room)"""

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
# hardcoded example for test_cross.txt, passes with 14 moves and all 9 rooms visited
# traversal_path = ['n', 'n', 's', 's', 'e', 'e', 'w', 'w', 'w', 'w', 'e','e', 's', 's']
"""traversal_path = []"""

# start_time = time.time()
# add rooms to graph.rooms dict 
# for i in range(0, len(world.rooms)):
#     graph.add_room(i) 
#     graph.rooms[i] = dict()
    # graph.rooms[i] = world.rooms[i].get_exits()
    # for exit in world.rooms[i].get_exits():
    #     graph.rooms[i].update({exit: '?'})
        
    # print(f'GRAPH ROOMS: {graph.rooms}')
    # print(f'RECURSVIE TRAVERSAL: {graph.dft_recursive(i)}')

# start = player.current_room.id
# graph.dft(start)
# print(f"PATH PROPERTY GRAPH CLASS: {graph.path}")
# player.travel('n', 'n')
# player.travel('n', 'n')
# end_time = time.time()

# print(f'CURRENT ROOM: {player.current_room.id}')
# print(f'GRAPH ROOMS: {graph.rooms}')
# print(f'NEIGHBORS: {graph.get_neighbors(1)}')
# print(f'TIME TO POPULATE GRAPH: {end_time - start_time} seconds')
# print(f'CURRENT_ROOM_ID: {player.current_room.id}')
# gives a list of directions as ['n', 's', 'e', 'w']
# exits_list = player.current_room.get_exits()
# print(f"TYPE: {type(exits_list)}")
# print(f'TRAVEL: {player.travel('n', 'n')}')