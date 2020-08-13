from room import Room
from player import Player
from world import World
from graph import Graph

import random
from ast import literal_eval

# Load world
world = World()
graph = Graph()

# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary --> reads from the different maps above and creates the 'text' for the map to generate
# prints out a dictionary of the rooms 
# value == a list of a tuple and a dictionary of directions
# What is in the tuple? 
# Ex --> 0: [(3,5), {'n': 1, 's': 5, 'e': 3, 'w': 7}]
# tuple represents (row, col) --> (row 3, col 5)
# room_graph --> list
room_graph=literal_eval(open(map_file, "r").read())
# print(f"LOOK HERE: \n\n {room_graph}, \n\n LEN OF ROOM_GRAPH: {len(room_graph)}")
# loads the rooms onto a graph
world.load_graph(room_graph)
# print(f'\n\n \t\t ROOMS[0][0]: {world.rooms[0]}, STARTING ROOM: {world.starting_room}')
# print(f'\n\n \t\t LOADED WORLD OUTPUT: {world.room_grid}') # --> output below can search for not None
# LOADED WORLD OUTPUT: [[None, None, None, None, None, None, None, None], [None, None, None, None, None, <room.Room object at 0x1056faf50>, None, None], [None, None, None, None, None, <room.Room object at 0x1056faf10>, None, None], [None, None, None, <room.Room object at 0x1056fadd0>, <room.Room object at 0x1056fad10>, <room.Room object at 0x1056fa510>, <room.Room object at 0x1056fa9d0>, <room.Room object at 0x1056faad0>], [None, None, None, None, None, <room.Room object at 0x1056fac90>, None, None], [None, None, None, None, None, <room.Room object at 0x1056fab50>, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None]]


# Print an ASCII map --> map view in the terminal
world.print_rooms()

# starting_room comes from world class 
# initialized as None, but after loading the rooms, is 000
# comes form world class self.rooms, initialized as an empty class that 
# is populated in def load_graph
player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
# hardcoded example for test_cross.txt, passes with 14 moves and all 9 rooms visited
# traversal_path = ['n', 'n', 's', 's', 'e', 'e', 'w', 'w', 'w', 'w', 'e','e', 's', 's']
traversal_path = []

# add rooms to graph.rooms dict 
for i in range(0, len(world.rooms)):
    graph.add_room(i) 
    graph.rooms[i] = world.rooms[i].get_exits()
    print(f'GRAPH ROOMS: {graph.rooms}')



print(f'CURRENT_ROOM_ID: {player.current_room.id}')
# gives a list of directions as ['n', 's', 'e', 'w']
# exits_list = player.current_room.get_exits()
# print(f"TYPE: {type(exits_list)}")
# print(f'TRAVEL: {player.travel('n', 'n')}')



# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
