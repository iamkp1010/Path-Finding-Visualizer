import math
import pygame as pg
from queue import PriorityQueue
import colors

totalHeight = 900
totalWidth = 900

# This is the Dijkstra algorithm 
# In this program we have taken same edge value between two cells for whole grid therefore we can say that this algo if BFS

# In Dijkstra, Min Priority Queue is used which is the implemention of the Min Heap data structure that will help us to find cell with 
# min distance in the priority Queue in Log(n) time where n is the heigth of the heap 

# Algo Explain:
# First we will push starting cell with distance 0 in the priorty queue
# after that we will pop out the top element in the PQ then we will push the adjacent cell to the current cells which are not Blocked
# this Process will continuosly run until either PQ empty or we have reached the End Cell


def reconstructPath(came_from, current, draw):  # after algo is over this function will create the path between Start Cell and End Cell
    while current in came_from:
        current = came_from[current]
        current.color = colors.WHITE
        draw()

# This is algo function 
def dijkstra(draw, grid, start, end):
    visited = {node: False for row in grid for node in row}     # This is the visited array which will helpful to check if cell is already visited or not
    distance = {node: math.inf for row in grid for node in row} # Storing the distance of Cur Cell and Start Cell such that we will get the min distance
    distance[start] = 0 
    came_from = {}
    priority_queue = PriorityQueue()       # intializing PQ
    priority_queue.put((0, start))         # pushing the start cell with distance 0

    while not priority_queue.empty():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
        current = priority_queue.get()[1]

        if visited[current]:
            continue
        visited[current] = True
        if current == end:
            reconstructPath(came_from, end, draw)
            return True
        if current != start:
            current.color = colors.CYAN
        for neighbor in current.neighbors:
            weight = 1
            if distance[current] + weight < distance[neighbor]:
                came_from[neighbor] = current
                distance[neighbor] = distance[current] + weight
                priority_queue.put((distance[neighbor], neighbor))
            if neighbor != end and neighbor != start and not visited[neighbor]:
                neighbor.color = colors.BLUE
        draw()
    
    print()
    print("There is no path between start and end!")
    return False