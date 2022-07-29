import pygame as pg
import colors

totalHeight = 900
totalWidth = 900

# This is the main class for node which represent the all cells in the grid (Nodes in Graph)
class Cell:

    # This is constructor of the Cell class which represent attributes of the particular cell object
    def __init__(self, row, column, width, total_rows):
        self.row = row               # to show current cell is in which row
        self.column = column         # to show current cell is in which coloumn 
        self.x = row * width         # this x value represent the cell's X axis position
        self.y = column * width      # this y value represent the cell's Y axis position
        self.color = colors.GREY     # to show color of the current Cell
        self.width = width           # width of the current row
        self.neighbors = []          # neighbours of current cell
        self.total_rows = total_rows # total number of rows in grid 

    # For finding the position of the current Cell
    def posFind(self):  
        return self.row, self.column

    # For drawing current cell into the grid
    def draw(self, window):
        pg.draw.rect(window, self.color, (self.x, self.y, self.width, self.width))

    # To update the neighbour of current cell such that neighbour cell is not blocked
    def updateNeighbors(self, grid):
        self.neighbors = []

        # this two array will be helpful to find neighbour of current cell
        # suppose current cell is at (4,3) then we will do (4+1,3+0) = (5,3) then (4-1,3+0) = (3,3) and the same.
        # this resultant cells are the neighbour of the current cell [ (4,3) in current example ]
        
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]

        for i in range(4):
            x = self.row + dx[i]
            y = self.column + dy[i]
            if (x >= 0 and x < self.total_rows and y >= 0 and y < self.total_rows and grid[x][y].color != colors.RED):
                self.neighbors.append(grid[x][y])

    # To compare two objects
    def __lt__(self, other):
        return False