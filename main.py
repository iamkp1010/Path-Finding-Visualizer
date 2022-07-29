import pygame as pg
from node import Cell
from astar import astar
from dijkstra import dijkstra
import colors

# total heigth and width for the grid
totalHeight = 900
totalWidth = 900

# for diplaying the window using pygame
window = pg.display.set_mode((totalHeight, totalWidth))

# Title for the window
pg.display.set_caption("Infosys Project")

# If we use mouse to mark cell then this syntax will helpful to get which button of the mouse is clicked
pm = pg.mouse

# This function will call the selected algorithm by giving the input from the keyboard
# If algo is 0 then it will call the ASTAR algo and if it is 1 then it will call the DIJKSTRA algo 
def algorithm(draw, grid, start, end, algo):
    if(algo == 0):
        astar(draw, grid, start, end)
    elif(algo == 1):
        dijkstra(draw, grid, start, end)

# to build the Grid
def buildGrid(row, width):
    grid = []                                           # this represent the whole grid
    node_width = width // row                           # Particular cell's width
    for i in range(row):
        temp = []                                       # this represent the only one row in the grid
        for j in range(row):
            temp.append(Cell(i, j, node_width, row))    # we will append the cells in row 
        grid.append(temp)                               # then we will append that row in the grid array such after all this iteration final grid will be ready 
    return grid


# this function will draw the lines between two cells such that they will look like grid
def drawGridLines(window, rows, width):
    gap = width // rows
    for i in range(rows):
        pg.draw.line(window, colors.BLACK, (0, i * gap), (width, i * gap))
        pg.draw.line(window, colors.BLACK, (i * gap, 0), (i * gap, width))

# this function will draw the grid
def draw(window, grid, rows, width):
    for row in grid:
        for node in row:
            node.draw(window)
    drawGridLines(window, rows, width)
    pg.display.update()

#this function will be helpful to get the position of clicked cell
def getClickedPosition(position, rows, width):
    gap = width // rows
    x, y = position
    row, column = x // gap, y // gap
    return (row, column)

# this is the main function which we will call first and the whole program start working after this
def main(window, totalWidth):
    ROWS = 90                               # total number of rows selected is 90 in the grid
    grid = buildGrid(ROWS, totalWidth)      # building the grid
    start, end = None, None                 # intialize the start and end points
    started = False                         # checking if algorithm is started or not
    algo = 0                                # by default algo is ASTAR
    loop = 1                                # while the value is 1 then program will run otherwise program will end 

    while loop:

        draw(window, grid, ROWS, totalWidth)    # this will continuosly draw the grid such that if any changes are done then it needs to be visible in the grid

        for event in pg.event.get():            # this is pygame attribute which is helpful to get the type of event we have done using either mouse or keyboard
            if event.type == pg.QUIT:           # if we close the window then QUIT event occures after which we need to just break out from this loop
                loop=0
            if started:                         # This shows that If algo is started then we can't do any changes in the grid
                continue

            if pm.get_pressed()[0]:             # If left button of mouse is pressed
                position = pm.get_pos()         # This will get us the cell position where the mouse button is pressed
                row, column = getClickedPosition(position, ROWS, totalWidth)
                node = grid[row][column]
                if not start and node != end:   # If we have not selected the start position then first selected cell will be the start cell
                    start = node
                    start.color = colors.ORANGE
                elif not end and node != start: # If we have not selected the end position after selecting the start position then second selected cell will be the end cell 
                    end = node
                    end.color = colors.GREEN
                elif node != start and node != end: # other then start cell and end cell, seleceted cell will be the Blocked Cell
                    node.color = colors.RED

            elif pm.get_pressed()[2]:   # If rightside button preseed then we just convert cell into the normal cell
                position = pm.get_pos()
                row, column = getClickedPosition(position, ROWS, totalWidth)
                node = grid[row][column]
                node.color = colors.GREY
                if node == start:
                    start = None
                if node == end:
                    end = None

            if event.type == pg.KEYDOWN:                    # If input is given by keyboard
                if event.key == pg.K_SPACE and not started: # If space is clicked then our selected algo will be started
                    started = True
                    for row in grid:
                        for node in row:
                            node.updateNeighbors(grid)      # we will update the neightbours first such that we will know that this cell is blocked or not
                    algorithm(lambda: draw(window, grid, ROWS, totalWidth), grid, start, end, algo) #calling the algorithm function to start algo
                    started = False         # algo is completed
                if event.key == pg.K_c:     # If we have to clear the grid then it can be done by pressing the C key
                    start = None
                    end = None
                    grid = buildGrid(ROWS, totalWidth)
                    draw(window, grid, ROWS, totalWidth)
                if(event.key == pg.K_d):    # If we have to select the DIJKSTRA algo then we need to press D key
                    algo = 1
                if(event.key == pg.K_a):    # A key for ASTAR algo
                    algo = 0
    
    pg.quit()


# calling the main function
main(window, totalWidth)


