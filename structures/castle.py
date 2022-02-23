import random
from utils import structuresUtils

from structures.door import Door
import managers.furnitureManager


def pickRectangleCastle(area):
    structureSizeX = 21
    structureSizeZ = 21
    structureX = random.randrange(
        area[0] + structureSizeX + 1, area[0] + area[2] - structureSizeX - 1)
    structureZ = random.randrange(
        area[1] + structureSizeZ + 1, area[1] + area[3] - structureSizeZ - 1)
    structureRect = (structureX, structureZ, structureSizeX, structureSizeZ)
    return structureRect


def buildCastle(rectangle, constructedRectangle, lowest_corner, height, doorsList):
    """Build a castle."""
    # clear the building area
    structuresUtils.setMultipleBlocks(rectangle[0], lowest_corner, rectangle[1], rectangle[2],
                                      lowest_corner + height + 1, rectangle[3], "air", "")

    # build main block
    structuresUtils.buildBlockFromCoord(constructedRectangle[0] + 7, constructedRectangle[1], 7, 19, 5, lowest_corner,
                                        "cobblestone")

    # build right tower block
    structuresUtils.buildBlockFromCoord(constructedRectangle[0], constructedRectangle[1] + 6, 8, 7, 10, lowest_corner,
                                        "cobblestone")

    # build left tower block
    structuresUtils.buildBlockFromCoord(constructedRectangle[0] + 13, constructedRectangle[1] + 6, 8, 7, 10, lowest_corner,
                                        "cobblestone")

    # door
    structuresUtils.buildDoorFromCoord(constructedRectangle[0] + 10, lowest_corner, constructedRectangle[1])

    d = Door()
    d.createDoor(rectangle[0] + 11, lowest_corner, rectangle[1] - 1, doorsList)

    # furniture
    managers.furnitureManager.createFurniture("castle", "chest", constructedRectangle, lowest_corner, "north")
    managers.furnitureManager.createFurniture("castle", "torch&windows", constructedRectangle, lowest_corner, "")
    managers.furnitureManager.createFurniture("castle", "spruce_stairs", constructedRectangle, lowest_corner, "south")

    # create towers entrance
    structuresUtils.setMultipleBlocks(constructedRectangle[0] + 7, lowest_corner + 1, constructedRectangle[1] + 8, 1,
                                      3, 3, "air", "")
    structuresUtils.setMultipleBlocks(constructedRectangle[0] + 13, lowest_corner + 1, constructedRectangle[1] + 8, 1
                                      , 3, 3, "air", "")

    # create carpets
    structuresUtils.setMultipleBlocks(constructedRectangle[0] + 10, lowest_corner, constructedRectangle[1], 1, 1, 17,
                                      "red_concrete", "")
    structuresUtils.setMultipleBlocks(constructedRectangle[0] + 2, lowest_corner, constructedRectangle[1] + 9, 17, 1, 1,
                                      "red_concrete", "")


    return d
