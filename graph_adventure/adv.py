from room import Room
from player import Player
from world import World
from roomGraphData import roomGraph
from util import Queue

import random

# Load world
world = World()

world.loadGraph(roomGraph)
world.printRooms()
player = Player("Name", world.startingRoom)


# FILL THIS IN
# traversalPath = ['n', 'n', 's']
traversalPath = []
traversalGraph = {}

for i in roomGraph:
    traversalGraph[i] = roomGraph[i][1]
print(traversalGraph)

# print(f"---{'n' in roomGraph[0][1].keys()}")

# qq = Queue()
# qq.enqueue(player.currentRoom.id)

# while qq:
#     room = qq.dequeue()
#     if room in traversalPath:
#         continue
#     traversalPath.append(room)
#     print(room)
#     if room is not None:
#         for adj_room in roomGraph[room][1].keys():
#             # print(roomGraph[room][1][adj_room])
#             qq.enqueue(roomGraph[room][1][adj_room])
#     else:
#         break

stack = []
stack.append(player.currentRoom.id)

while stack:
    room = stack.pop()
    if room in traversalPath:
        continue

    print(room)
    if room is not None and room in traversalGraph.keys():
        # exits = player.currentRoom.getExits()

        for side in player.currentRoom.getExits():
            path = (player.currentRoom.id, side)
            if path not in traversalPath:
                player.travel(side)
                traversalPath.append(path)
                stack.append(player.currentRoom.id)
    else:
        break

print('---------------------------------|||||||\n\n')
print(f'{traversalPath}')
print('\n\n')



# traversalPath = ['e', 'e', 'w', 'w', 'w', 'w',
#                  'e', 'e', 's', 's', 'n', 'n', 'n', 'n']

traversalPath = [i[1] for i in traversalPath]

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


#######
# UNCOMMENT TO WALK AROUND
#######
# player.currentRoom.printRoomDescription(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     else:
#         print("I did not understand that command.")
