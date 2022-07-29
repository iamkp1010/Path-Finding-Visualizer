import math
import pygame as pg
from queue import PriorityQueue
import colors

# This is the ASTAR algorithm
# We have used PQ to get the min distance among all the cells that are in the PQ
# This will take Log(N) time to push cell into the PQ

# Algo Explain:

# In ASTAR algorithm there is distance function which represent the distance between the Cur cell and End Cell
# We will select the cell which is nearest to the End Cell
# DistFun = H() + G()

# here H function is the HuresticFuction which will give the huerstic distance between Cur cell and End cell
# I have used Manhatten Distance
# here G function represent the normal distance we have used in the dijkstra algo

# This alog is very fast compare to other alog becasuse of the huresticFunction, from that we can skip the extra iteration of other cell that are
# farthest to the End cell

totalHeight = 900
totalWidth = 900

def reconstructPath(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.color = colors.WHITE
        draw()

def huresticFunction(intermediate_node, end_node):
    x1, y1 = intermediate_node
    x2, y2 = end_node
    return abs(x1 - x2) + abs(y1 - y2)

def astar(draw, grid, start, end):

    count = 0
    priority_queue = PriorityQueue()
    priority_queue.put((0, count, start))
    came_from = {}
    g_score = {node: math.inf for row in grid for node in row}
    g_score[start] = 0
    f_score = {node: math.inf for row in grid for node in row}
    f_score[start] = huresticFunction(start.posFind(), end.posFind())
    open_set = {start}

    while not priority_queue.empty():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
        current = priority_queue.get()[2]
        open_set.remove(current)
        if current == end:
            reconstructPath(came_from, end, draw)
            return True
        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + huresticFunction(
                    neighbor.posFind(), end.posFind()
                )
                if neighbor not in open_set:
                    count += 1
                    priority_queue.put((f_score[neighbor], count, neighbor))
                    open_set.add(neighbor)
                    if neighbor != end:
                        neighbor.color = colors.BLUE
        draw()
        if current != start:
            current.color = colors.CYAN
    
    print()
    print("There is no path between start and end!")
    return False