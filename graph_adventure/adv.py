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
# qq.enqueue(0)

# while qq:
#     vertex = qq.dequeue()
#     if vertex in traversalPath:
#         continue
#     traversalPath.append(vertex)
#     print(vertex)
#     if vertex is not None:
#         for adj_vertex in roomGraph[vertex][1].keys():
#             # print(roomGraph[vertex][1][adj_vertex])
#             qq.enqueue(roomGraph[vertex][1][adj_vertex])
#     else:
#         break

# stack = []
# stack.append(3)

# while stack:
#     vertex = stack.pop()
#     if vertex in traversalPath:
#         continue

#     print(vertex)
#     if vertex is not None and vertex in roomGraph:
#         traversalPath.append(vertex)
#         print(vertex)
#         for adj_vertex in roomGraph[vertex][1].keys():
#             stack.append(roomGraph[vertex][1][adj_vertex])
#     else:
#         break

# print('---------------------------------|||||||\n\n')
# print(f'{traversalPath}')
# print('\n\n')

traversalPath = ['e', 'e', 'w', 'w', 'w', 'w',
                 'e', 'e', 's', 's', 'n', 'n', 'n', 'n']

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
