import random
from utils import util, structuresUtils
from structures.door import Door
import managers.furnitureManager



def pickRectangleChurch(area):
    structureSizeX = 16
    structureSizeZ = 16
    structureX = area[2] // 2 - 8
    structureZ = area[3] // 2 - 8
    structureRect = (structureX, structureZ, structureSizeX, structureSizeZ)
    return structureRect


def buildChurch(rectangle, constructedRectangle, lowest_corner, height, doorsList):
    """Build a church."""

    # clear the building area
    structuresUtils.setMultipleBlocks(rectangle[0], lowest_corner, rectangle[1], rectangle[2],
                                      lowest_corner + height + 1, rectangle[3], "air", "")

    # build a block
    structuresUtils.buildBlockFromRec(constructedRectangle, lowest_corner, height, "spruce_log", "cobblestone",
                                      "cobblestone")

    # build a cross
    buildCross(constructedRectangle, lowest_corner, height, "gold_block")

    # build a door
    structuresUtils.buildDoorFromCoord(constructedRectangle[0] + 6, lowest_corner, constructedRectangle[1])

    d = Door()
    d.createDoor(rectangle[0] + 7, lowest_corner, rectangle[1] - 1, doorsList)

    # build furniture
    typeList = ["type1", "type2"]
    churchType = random.choice(typeList)
    print(churchType)
    if churchType == "type1":
        managers.furnitureManager.createFurniture("church", "spruce_stairs", constructedRectangle, lowest_corner,
                                                  churchType)
    else:
        managers.furnitureManager.createFurniture("church", "spruce_stairs", constructedRectangle, lowest_corner,
                                                  churchType)

    return d

def buildCross(rec, lowest_corner, height, crossMaterial):
    for y in range(lowest_corner + height + 1, lowest_corner + height + 9):
        for x in range(rec[0] + 6, rec[0] + rec[2] - 6):
            for z in range(rec[1] + 6, rec[1] + rec[3] - 6):
                util.setBlockBatched(x, y, z, crossMaterial)

    for y in range(lowest_corner + height + 5, lowest_corner + height + 7):
        for x in range(rec[0] + 4, rec[0] + rec[2] - 4):
            for z in range(rec[1] + 6, rec[1] + rec[3] - 6):
                util.setBlockBatched(x, y, z, crossMaterial)