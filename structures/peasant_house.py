import random
from utils import structuresUtils
import managers.furnitureManager

from structures.door import Door

def pickRectanglePeasantHouse(area):
    structureSizeX = random.randrange(9, 11)
    structureSizeZ = random.randrange(9, 11)
    structureX = random.randrange(
        area[0] + structureSizeX + 1, area[0] + area[2] - structureSizeX - 1)
    structureZ = random.randrange(
        area[1] + structureSizeZ + 1, area[1] + area[3] - structureSizeZ - 1)
    structureRect = (structureX, structureZ, structureSizeX, structureSizeZ)
    return structureRect

def buildPeasantHouse(rectangle, constructedRectangle, lowest_corner, height, doorsList):
    """Build a small house."""
    # clear the building area
    structuresUtils.setMultipleBlocks(rectangle[0], lowest_corner, rectangle[1], rectangle[2],
                                      lowest_corner + height + 1, rectangle[3], "air", "")

    # build the block
    structuresUtils.buildBlockFromRec(constructedRectangle, lowest_corner, height, "oak_planks", "spruce_wood", "spruce_log")

    # build a triangle roof
    structuresUtils.buildTriangleRoof(constructedRectangle, lowest_corner, height, "spruce_log")

    # build a door and furniture
    isZLonger = structuresUtils.buildDoorFromRec(constructedRectangle, lowest_corner)
    #isZLonger = structuresUtils.isZLonger(constructedRectangle, lowest_corner)

    if isZLonger:
        # build a door
        d = Door()
        d.createDoor(rectangle[0] - 1, lowest_corner, rectangle[1] + 4, doorsList)

        #build furniture
        managers.furnitureManager.createFurniture("peasant_house", "all", constructedRectangle, lowest_corner, "z_longer")

    elif not isZLonger:
        # build a door
        d = Door()
        d.createDoor(rectangle[0] + 4, lowest_corner, rectangle[1] - 1, doorsList)

        # build furniture
        managers.furnitureManager.createFurniture("peasant_house", "all", constructedRectangle, lowest_corner, "x_longer")

    return d





