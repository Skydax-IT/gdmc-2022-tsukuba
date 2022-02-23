import random
from utils import interfaceUtils, util, structuresUtils

from structures.door import Door
import managers.furnitureManager


def pickRectangleFarm(area):
    structureSizeX = 14
    structureSizeZ = 14
    structureX = random.randrange(
        area[0] + structureSizeX + 1, area[0] + area[2] - structureSizeX - 1)
    structureZ = random.randrange(
        area[1] + structureSizeZ + 1, area[1] + area[3] - structureSizeZ - 1)
    structureRect = (structureX, structureZ, structureSizeX, structureSizeZ)
    return structureRect

def buildFarm(rectangle, constructedRectangle, lowest_corner, height, doorsList):
    """Build a farm."""
    # clear the building area
    structuresUtils.setMultipleBlocks(rectangle[0], lowest_corner, rectangle[1], rectangle[2],
                                      lowest_corner + height + 1, rectangle[3], "air", "")

    # build main block
    structuresUtils.buildBlockFromCoord(constructedRectangle[0], constructedRectangle[1], 7, constructedRectangle[3], 4, lowest_corner,
                                        "hay_block")

    # build the door
    structuresUtils.buildDoorFromCoord(constructedRectangle[0] + 3, lowest_corner, constructedRectangle[1])

    d = Door()
    d.createDoor(rectangle[0] + 4, lowest_corner, rectangle[1] - 1, doorsList)

    # build grass block
    structuresUtils.buildBlockFromCoord(constructedRectangle[0] + 7, constructedRectangle[1], 7,
                                        constructedRectangle[3], 0, lowest_corner, "grass_block")

    # build animals fence
    buildAnimalsFence(constructedRectangle[0] + 7, constructedRectangle[1], 7, constructedRectangle[3], lowest_corner + 1, "oak")

    # build main block's side entrance (could be a function)
    structuresUtils.setMultipleBlocks(constructedRectangle[0] + 6, lowest_corner + 1, constructedRectangle[1] + 4, 2,
                                      2, 4, "air", "")
    structuresUtils.setMultipleBlocks(constructedRectangle[0] + 6, lowest_corner + 1, constructedRectangle[1] + 5, 1,
                                      1, 2, "oak_fence_gate", "east")
    util.setBlockBatched(constructedRectangle[0] + 6, lowest_corner + 1, constructedRectangle[1] + 4, "oak_fence")
    util.setBlockBatched(constructedRectangle[0] + 6, lowest_corner + 1, constructedRectangle[1] + 7, "oak_fence")

    # furniture
    managers.furnitureManager.createFurniture("farm", "all", constructedRectangle, lowest_corner, "north")

    # summon animals
    summonAnimal(constructedRectangle[0] + 8, lowest_corner + 1, constructedRectangle[1] + 2, "cow", 4)
    summonAnimal(constructedRectangle[0] + 8, lowest_corner + 1, constructedRectangle[1] + 2, "donkey", 1)
    summonAnimal(constructedRectangle[0] + 8, lowest_corner + 1, constructedRectangle[1] + 2, "chicken", 2)

    return d

def buildAnimalsFence(x, z, xSize, zSize, y, fenceMaterial):
    structuresUtils.setMultipleBlocks(x, y, z, xSize, 1, 1, f"{fenceMaterial}_fence", "")
    structuresUtils.setMultipleBlocks(x, y, z, 1, 1, zSize, f"{fenceMaterial}_fence", "")

    structuresUtils.setMultipleBlocks(x, y, z + zSize - 1, xSize, 1, 1, f"{fenceMaterial}_fence", "")
    structuresUtils.setMultipleBlocks(x + xSize - 1, y, z, 1, 1, zSize, f"{fenceMaterial}_fence", "")

def summonAnimal(x, y, z, animalType, populationNumber):
    while populationNumber != 0:
        interfaceUtils.runCommand(f"summon minecraft:{animalType} {x} {y} {z}")
        populationNumber = populationNumber - 1