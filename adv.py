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
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

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
path = list()
curr = player.current_room
reverse_exits = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}

# start by adding the player.current_room.id to visited
visited.append(curr.id)
# also to path to view
path.append(curr.id)
# initialize the room num with an empty dictionary
rooms[curr.id] = dict()
# get the exits and for each exit, assign it '?'
for room_exits in curr.get_exits():
    rooms[curr.id][room_exits] = '?'

# make a function to choose a path that takes a room_id
def choose_path(room_id):
    # for each exit in the dict of rooms[room_id]
    for exit in rooms[room_id]:
        # check if it has '?'
        if rooms[room_id][exit] == '?':
            # if so return that exit
            return exit

    # remove the last item from visited
    del visited[-1]
    # take that room number and loop through the exits (key) and room numbers (value)
    for new_exit, room_num in rooms[visited[-1]].items():
        # check if the room number is the same as the current room
        if room_num == room_id:
            # if yes, return the opposite to go back
            return reverse_exits[new_exit]

# print(f"CURRENT ROOM ID: {player.current_room.id}")
# while the length of the rooms dict is less than the length of the world.rooms dict runt eh following code
while len(rooms) < len(world.rooms):
    # create a move variable to store the current room id direction to go in (which exit to take), either a new one if it's '?' or reverse if
    move = choose_path(player.current_room.id)
    # make the player move in the direction of the exit
    player.travel(move)
    # print(f"CURRENT ROOM ID: {player.current_room.id}")
    # add that exit to the traversal path list to run the code below
    traversal_path.append(move)
    # print(f"TRAVERSAL INSIDE: {traversal_path}")
    # print(f"ROOMS INSIDE: {rooms}")
    # print(f"VISITED: {visited[-1]}")

    #check if the current room id is the same as the last room id in visited, if the player moved, it should be different
    if player.current_room.id is not visited[-1]:
        # if yes, append the id to visited
        visited.append(player.current_room.id)
        # and the path, just to see
        path.append(player.current_room.id)
    # check if the current room id is not in the room dict keys
    if player.current_room.id not in rooms.keys():
        # if yes, initialize an empty dict
        rooms[player.current_room.id] = dict()
        # get the exits and assign '?' to the exit directions
        for new_exit in player.current_room.get_exits():
            rooms[player.current_room.id][new_exit] = '?'
    # check if the current room id opposite is '?'
    if rooms[player.current_room.id][reverse_exits[move]] == '?':
        # if yes, take the second from last room id in visited (the previous room) and assign it to that direction
        rooms[visited[-2]][move] = player.current_room.id
        # take the opposite of the current room id and assign it to the second from last room id in visited
        rooms[player.current_room.id][reverse_exits[move]] = visited[-2]

# print(f"ROOMS: {rooms}")
# print(f"VISITED: {visited}")
# print(f"PATH: {path}")
# print(f"TRAVERSAL: {traversal_path}")

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
