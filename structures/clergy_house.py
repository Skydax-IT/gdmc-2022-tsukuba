import random
from utils import structuresUtils
from structures.door import Door
import managers.furnitureManager

typeList = ["blue", "red"]

def pickRectangleClergyHouse(area):
    structureSizeX = 11
    structureSizeZ = 11
    structureX = random.randrange(
        area[0] + structureSizeX + 1, area[0] + area[2] - structureSizeX - 1)
    structureZ = random.randrange(
        area[1] + structureSizeZ + 1, area[1] + area[3] - structureSizeZ - 1)
    structureRect = (structureX, structureZ, structureSizeX, structureSizeZ)
    return structureRect

def buildClergyHouse(rectangle, constructedRectangle, lowest_corner, height, doorsList):
    """Build a clergy house."""

    # clear the building area
    structuresUtils.setMultipleBlocks(rectangle[0], lowest_corner, rectangle[1], rectangle[2],
                                      lowest_corner + height + 1, rectangle[3], "air", "")

    # block
    structuresUtils.buildBlockFromRec(constructedRectangle, lowest_corner, height, "bricks", "oak_wood", "oak_wood")

    # roof
    structuresUtils.buildTriangleRoof(constructedRectangle, lowest_corner, height, "oak_wood")

    # door
    structuresUtils.buildDoorFromCoord(constructedRectangle[0] + 3, lowest_corner, constructedRectangle[1])

    d = Door()
    d.createDoor(rectangle[0] + 4, lowest_corner, rectangle[1] - 1, doorsList)

    # furniture
    clergyType = random.choice(typeList)
    print(clergyType)
    if clergyType == "red":
        managers.furnitureManager.createFurniture("clergy_house", "all", constructedRectangle, lowest_corner,
                                                  clergyType)
        typeList.remove("red")
    else:
        managers.furnitureManager.createFurniture("clergy_house", "all", constructedRectangle, lowest_corner,
                                                  clergyType)
        typeList.remove("blue")


    return d