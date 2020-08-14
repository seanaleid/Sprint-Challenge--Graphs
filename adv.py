from room import Room
from player import Player
from world import World
from utils import Queue, Stack

import random
from ast import literal_eval
import time 

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map --> map view in the terminal
world.print_rooms()
# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
player = Player(world.starting_room)

""" Set up my variables to use"""

rooms = dict()
visited = list()
curr = player.current_room.id

# populate graph
for i in range(0, len(world.rooms)):
    rooms[i] = dict()

    for exit in world.rooms[i].get_exits():
        # print(f"TEST TEST TEST: {world.rooms[i].n_to.id}")
        # print(f"ANOTHER TEST: {world.rooms[i].get_exits_id(exit)}")
        room_num = world.rooms[i].get_exits_id(exit)
        rooms[i].update({exit: room_num})
        
print(f'GRAPH ROOMS: {rooms}')

# print(f'CURRENT_ROOM: {player.current_room.get_exits()}')

def dft(starting_room):
    s = Stack()
    s.push(starting_room)    

    while s.size() > 0 and len(visited) < len(rooms):
        r = s.pop()
        # print(f"rrrrrr {r}")
        print(f"CURR: {r}")
        if r not in visited:
            visited.append(r)
        neighbors = rooms[r]
        # print(f'neighbors: {neighbors}')

        for neighbor, value in neighbors.items():
            if value not in visited:
                traversal_path.append(neighbor)
                s.push(value)
    print(f'PATH: {traversal_path}')

print(f"TRAVERSAL: {traversal_path}")
dft(curr)


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
