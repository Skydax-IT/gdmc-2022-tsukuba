#! /usr/bin/python3
"""
Author: Enzo Licata
This code generates a simple Minecraft village.
It is intended to participate in the GDMC competition.
"""
__all__ = []
# __version__
import random

from utils import interfaceUtils, mapUtils
from utils.worldLoader import WorldSlice

from managers import gridManager
from managers.structureManager import Structure
from road.road import Road
import structures.door
import structures.fence
import managers
import biome

# Do we send blocks in batches to speed up the generation process?
USE_BATCHING = True

#util.getPos()

# x position, z position, x size, z size
area = (0, 0, 100, 100)  # default build area

# see if a build area has been specified
# you can set a build area in minecraft using the /setbuildarea command
buildArea = interfaceUtils.requestBuildArea()
if buildArea != -1:
    x1 = buildArea["xFrom"]
    z1 = buildArea["zFrom"]
    x2 = buildArea["xTo"]
    z2 = buildArea["zTo"]
    # print(buildArea)
    area = (x1, z1, x2 - x1, z2 - z1)

# get and print the biome ID
biome = biome.Biome()
biomeId = biome.getBiome(area[0], area[1], 10, 10)
print("Biome ID : " + biomeId)

# tp to the build area
interfaceUtils.runCommand(f"tp @p {area[0]} 100 {area[1]}")

# doors list + houses list
doorsList = []
houses = []

# 2D grid
grid = []

if __name__ == '__main__':

    if biomeId != "":
        """Generate a village within the target area."""
        print(f"Build area is at position {area[0]}, {area[1]} with size {area[2]}, {area[3]}")

        """#clear all
        for y in range(60, 73):
            for x in range(area[0], area[2]):
                for z in range(area[1], area[3]):
                    util.setBlockBatched(x, y, z, "air")"""

        # load the world data
        # this uses the /chunks endpoint in the background
        worldSlice = WorldSlice(area)

        # calculate a heightmap suitable for building:
        heightmap = mapUtils.calcGoodHeightmap(worldSlice)

        # example alternative heightmaps:
        #heightmap = worldSlice.heightmaps["MOTION_BLOCKING"]
        # heightmap = worldSlice.heightmaps["MOTION_BLOCKING_NO_LEAVES"]
        # heightmap = worldSlice.heightmaps["OCEAN_FLOOR"]
        #heightmap = worldSlice.heightmaps["WORLD_SURFACE"]

        # show the heightmap as an image
        #mapUtils.visualize(heightmap, title="heightmap")

        # build a fence around the perimeter
        structures.fence.buildFence(heightmap, area)

        # build a church
        church = Structure("church")
        church.buildStructure(doorsList, houses, heightmap, area)
        houses.append(church.rectangle)

        # build a castle
        castle = Structure("castle")
        castle.buildStructure(doorsList, houses, heightmap, area)
        houses.append(castle.rectangle)

        #build a farm
        farm = Structure("farm")
        farm.buildStructure(doorsList, houses, heightmap, area)
        houses.append(farm.rectangle)

        # build peasants houses
        for i in range(random.randrange(5, 8)):
            newHouse = Structure("peasant_house")
            newHouse.buildStructure(doorsList, houses, heightmap, area)
            houses.append(newHouse.rectangle)

        # build clergy houses
        for j in range(2):
            clergy_house = Structure("clergy_house")
            clergy_house.buildStructure(doorsList, houses, heightmap, area)
            houses.append(clergy_house.rectangle)

        if USE_BATCHING:
            # we need to send any blocks remaining in the buffer
            interfaceUtils.sendBlocks()
    else:
        print("The biome ID from the buildarea is different from biome ID: " + biomeId)

    # sort the doors list
    doorsList = structures.door.getSortedList(doorsList)

    # create a grid
    grid = gridManager.initializeGrid(area)

    # update the grid with obstacles
    for house in houses:
        grid = gridManager.updateGrid(house, grid)

    # update the heightmap
    heightmap = mapUtils.calcGoodHeightmap(worldSlice)

    # build the classic roads
    i = 0  # initialize i
    while i < len(doorsList) - 1:  # loop until all doors are linked (compute a path and build a mc road)
        start = (doorsList[i].z, doorsList[i].x)
        goal = (doorsList[i + 1].z, doorsList[i + 1].x)

        newRoad = Road("white")
        grid = newRoad.buildRoad(grid, start, goal, heightmap, area)

        i += 1  # increment i

    # build specific roads
    structuresList = managers.structureManager.getstructuresList()
    goalList = []
    for h in structuresList:
        if h.structureType == "church":
            startSpecificRoad = (h.door.z, h.door.x)
        if h.structureType == "clergy_house":
            goalSpecificRoad = (h.door.z, h.door.x)
            goalList.append(goalSpecificRoad)

    for g in goalList:
        newSRoad = Road("yellow")
        print(f"building a specific road from {startSpecificRoad} to {g} = (z,x)")
        grid = newSRoad.buildRoad(grid, startSpecificRoad, g, heightmap, area)

    # plot the map
    gridManager.plotGrid(grid)



