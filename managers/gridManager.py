"""Initialize and update the 2D grid from the build area"""
import numpy as np
from matplotlib import pyplot as plt

"""_____GRID CONTROLLER_____"""
# create a grid representing the build area
def initializeGrid(area):
    zSize = area[3] - area[1] + 1
    xSize = area[2] - area[0] + 1
    grid = np.zeros((zSize, xSize), dtype=int)
    return grid


# update the grid by adding obstacles
def updateGrid(h, grid):
    for row in range(h[1], h[1] + h[3]):
        for column in range(h[0], h[0] + h[2]):
            grid[row][column] = 1
    return grid


# update the grid by representing the path
def updatePathGrid(start, goal, path, grid):
    # the number "2" represents the start
    grid[start[0], start[1]] = 2


    # the number "3" represents the path
    for tile in path:
        grid[tile[0], tile[1]] = 3

    # the number "4" represents the goal
    grid[goal[0], goal[1]] = 4

    return grid


# plot the grid
def plotGrid(grid):
    plt.title('Shortest paths with A*')
    plt.imshow(grid)
    plt.show()





