from room import Room
from player import Player
from world import World
from roomGraphData import roomGraph
from util import Queue
import random

import random

# Load world
world = World()

world.loadGraph(roomGraph)
world.printRooms()
player = Player("Name", world.startingRoom)

# FILL THIS IN
traversalPath = ['n', 's']


exploration_map = {}
# Find all possible exits
possible_exits = player.currentRoom.getExits()
exploration_map[player.currentRoom.id] = {i: '?' for i in possible_exits}
# Keep track of all unexplored rooms
unexplored_rooms = []
for option in player.currentRoom.getExits():
    # Add the option to the unexplored rooms
    unexplored_rooms.append({(player.currentRoom.id, option)})
while unexplored_rooms:
    # Execute a DFS until we reach a room with no unexplored paths
    if '?' in exploration_map[player.currentRoom.id].values():
        # Create a helper function to go backwards
        def reverse_direction(direction):
            if direction is 'n':
                return 's'
            elif direction is 's':
                return 'n'
            elif direction is 'e':
                return 'w'
            elif direction is 'w':
                return 'e'
        next_move = None
        starting_room = player.currentRoom.id
        # Find an unexplored exit and move towards it
        if 'n' in exploration_map[starting_room] and exploration_map[starting_room]['n'] == '?':
            next_move = 'n'
        elif 'e' in exploration_map[starting_room] and exploration_map[starting_room]['e'] == '?':
            next_move = 'e'
        elif 's' in exploration_map[starting_room] and exploration_map[starting_room]['s'] == '?':
            next_move = 's'
        elif 'w' in exploration_map[starting_room] and exploration_map[starting_room]['w'] == '?':
            next_move = 'w'
        # Remove the next room from the unexplored_rooms
        unexplored_rooms.remove({(player.currentRoom.id, next_move)})

        # Move on to the next room
        player.travel(next_move)
        # Add every new move to the traversalPath
        new_room = player.currentRoom.id
        traversalPath.append(next_move)
        # If the new room is not in the exploration_map, find the possible exits
        if new_room not in exploration_map:
            exploration_map[new_room] = {
                i: '?' for i in player.currentRoom.getExits()}
        # Update the exploration map
        exploration_map[starting_room][next_move] = new_room
        exploration_map[new_room][reverse_direction(next_move)] = starting_room
        # Add all unexplored rooms to the unexplored_rooms list
        for available_exit, room_id in exploration_map[new_room].items():
            if room_id == '?':
                unexplored_rooms.append({(new_room, available_exit)})
        # If exploration_map has 500 entries and there are no '?' left then break out of the loop
        if len(list(exploration_map)) == 500 and '?' not in exploration_map[player.currentRoom.id].values():
            break
    else:
        # If all of the unexplored exits have been discovered in the current room...
        # Execute a BFS to find the shortest path to an unexplored room
        starting_room = player.currentRoom.id
        q = Queue()
        for available_exit, room_id in exploration_map[starting_room].items():
            # Enqueue a path to the available exits and the rooms leading from them
            q.enqueue([[available_exit, room_id]])
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first path
            path = q.dequeue()
            # Grab the room from the path
            room = path[-1]
            # If all exits have been explored in the room we moved backwards into...
            if '?' not in [room_id for available_exit, room_id in exploration_map[room[1]].items()]:
                for available_exit, room_id in exploration_map[room[1]].items():
                    # If the exit doesn't lead to the path or the current room
                    if room_id is not starting_room and room_id not in [room_id for available_exit, room_id in path]:
                        # Copy the path
                        new_path = list(path)
                        # Append the available exit and the room connected to it to the new path
                        new_path.append([available_exit, room_id])
                        q.enqueue(new_path)
            else:
                # Loop through the current room's available exits and the id's of the rooms they lead to...
                for available_exit, room_id in path:
                    # Move into that direction
                    player.travel(available_exit)
                    # Add the discovered exit to the traversal path
                    traversalPath.append(available_exit)
                break
# TRAVERSAL TEST
visited_rooms = set()
player.currentRoom = world.startingRoom
visited_rooms.add(player.currentRoom)
for move in traversalPath:
    player.travel(move)
    visited_rooms.add(player.currentRoom)
if len(visited_rooms) == len(roomGraph):
    print(
        f"TESTS PASSED: {len(traversalPath)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(roomGraph) - len(visited_rooms)} unvisited rooms")
######
# UNCOMMENT TO WALK AROUND
######
# player.currentRoom.printRoomDescription(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     else:
#         print("I did not understand that command.")
