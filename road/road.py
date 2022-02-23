import astarPathFinder
from managers import gridManager
from utils import interfaceUtils, util


class Road:
    """Definition of a Road"""

    def __init__(self, color):
        self.color = color
        self.roadPath = []

    def createRoadPath(self, start, path):
        roadPathBuffer = path
        roadPathBuffer.append(start)
        roadPathBuffer.reverse()
        roadPathBuffer.pop()
        self.roadPath = roadPathBuffer

    def buildRoad(self, grid, start, goal, heightmap, area):
        path = astarPathFinder.computePath(grid, start, goal)  # compute the path between two doors
        grid = gridManager.updatePathGrid(start, goal, path, grid)  # add the path to the grid (can be improved)
        self.createRoadPath(start, path)

        previousHeight = util.heightAt(start[1], start[0], heightmap, area)
        iteration = 1
        for block in self.roadPath:
            x = block[1]
            z = block[0]
            y = util.heightAt(x, z, heightmap, area)

            """if iteration == len(self.roadPath):
                if y > previousHeight + 1:
                    self.fillTheRoadUp(x, y, z, previousHeight)
                else:
                    pass"""

            if y > previousHeight + 1:
                y = previousHeight + 1
            elif y < previousHeight - 1:
                y = previousHeight - 1

            util.setBlockBatched(x, y - 1, z, f"{self.color}_concrete")
            util.setBlockBatched(x, y, z, "air")
            util.setBlockBatched(x, y + 1, z, "air")

            previousHeight = y
            iteration += 1

        interfaceUtils.sendBlocks()
        return grid

    """def fillTheRoadUp(self, x, y, z, previousHeight):
        print(f"FILLING THE ROAD UP at {x} {z}")
        currentHeight = previousHeight
        while currentHeight != y:
            util.setBlockBatched(x + 1, currentHeight + 1,  z, f"{self.color}_concrete")
            currentHeight += 1
            print({f"we are at {currentHeight}"})"""


