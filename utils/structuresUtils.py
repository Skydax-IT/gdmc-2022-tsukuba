from utils import util


def buildBlockFromRec(rec, lowest_corner, height, wallsMaterial, cornersMaterial, roofMaterial):
    # floor
    for x in range(rec[0], rec[0] + rec[2]):
        for z in range(rec[1], rec[1] + rec[3]):
            util.setBlockBatched(x, lowest_corner, z, "cobblestone")

    # walls
    for y in range(lowest_corner + 1, lowest_corner + height):
        for x in range(rec[0] + 1,
                       rec[0] + rec[2] - 1):
            util.setBlockBatched(x, y, rec[1], wallsMaterial)
            util.setBlockBatched(x, y, rec[1] + rec[3] - 1, wallsMaterial)
        for z in range(rec[1] + 1,
                       rec[1] + rec[3] - 1):
            util.setBlockBatched(rec[0], y, z, wallsMaterial)
            util.setBlockBatched(rec[0] + rec[2] - 1, y, z, wallsMaterial)

    # corners
    for dx in range(2):
        for dz in range(2):
            x = rec[0] + dx * (
                    rec[0] + rec[2] - rec[0] - 1)
            z = rec[1] + dz * (
                    rec[1] + rec[3] - rec[1] - 1)
            for y in range(lowest_corner, lowest_corner + height):
                util.setBlockBatched(x, y, z, cornersMaterial)

    # clear interior
    for y in range(lowest_corner + 1, lowest_corner + height):
        for x in range(rec[0] + 1,
                       rec[0] + rec[2] - 1):
            for z in range(rec[1] + 1,
                           rec[1] + rec[3] - 1):
                util.setBlockBatched(x, y, z, "air")

    # roof
    for x in range(rec[0], rec[0] + rec[2]):
        for z in range(rec[1], rec[1] + rec[3]):
            util.setBlockBatched(x, lowest_corner + height, z, roofMaterial)


def buildTriangleRoof(rec, lowest_corner, height, tRoofMaterial):
    # triangle roof
    if rec[0] + rec[2] - rec[0] < \
            rec[1] + rec[3] - rec[1]:
        for i in range(0, rec[0] + rec[2] - rec[0],
                       2):
            halfI = int(i / 2)
            for x in range(rec[0] + halfI,
                           rec[0] + rec[2] - halfI):
                for z in range(rec[1],
                               rec[1] + rec[3]):
                    util.setBlockBatched(x, lowest_corner + height + halfI, z, tRoofMaterial)

    else:
        # same as above but with x and z swapped
        for i in range(0, rec[1] + rec[3] - rec[1],
                       2):
            halfI = int(i / 2)
            for z in range(rec[1] + halfI,
                           rec[1] + rec[3] - halfI):
                for x in range(rec[0],
                               rec[0] + rec[2]):
                    util.setBlockBatched(x, lowest_corner + height + halfI, z, tRoofMaterial)


def buildDoorFromRec(rec, lowest_corner):
    if rec[0] + rec[2] - rec[0] < \
            rec[1] + rec[3] - rec[1]:
        for y in range(lowest_corner + 1, lowest_corner + 2):
            util.setBlockBatched(rec[0], y, rec[1] + 3, "air")

        util.setBlockBatched(rec[0], lowest_corner + 1, rec[1] + 3,
                             "oak_door[half=lower]")
        util.setBlockBatched(rec[0], lowest_corner + 2, rec[1] + 3,
                             "oak_door[half=upper]")
        util.setBlockBatched(rec[0] - 1, lowest_corner, rec[1] + 3,
                             "red_concrete")
        util.setBlockBatched(rec[0] - 1, lowest_corner + 3, rec[1] + 3,
                             "wall_torch[facing=west]")
        return True

    else:
        for y in range(lowest_corner + 1, lowest_corner + 2):
            util.setBlockBatched(rec[0] + 3, y, rec[1], "air")

        util.setBlockBatched(rec[0] + 3, lowest_corner + 1, rec[1],
                             "oak_door[half=lower]")
        util.setBlockBatched(rec[0] + 3, lowest_corner + 2, rec[1],
                             "oak_door[half=upper]")
        util.setBlockBatched(rec[0] + 3, lowest_corner, rec[1] - 1,
                             "red_concrete")
        util.setBlockBatched(rec[0] + 3, lowest_corner + 3, rec[1] - 1,
                             "wall_torch[facing=north]")
        return False

def buildBlockFromCoord(xCoord, zCoord, xSize, zSize, height, lowest_corner, blockMaterial):
    #floor
    for x in range(xCoord, xCoord + xSize):
        for z in range(zCoord, zCoord + zSize):
            util.setBlockBatched(x, lowest_corner, z, blockMaterial)

    #walls
    for y in range(lowest_corner + 1, lowest_corner + height):
        for x in range(xCoord, xCoord + xSize):
            util.setBlockBatched(x, y, zCoord, blockMaterial)
            util.setBlockBatched(x, y, zCoord + zSize - 1, blockMaterial)
        for z in range(zCoord, zCoord + zSize):
            util.setBlockBatched(xCoord, y, z, blockMaterial)
            util.setBlockBatched(xCoord + xSize - 1, y, z, blockMaterial)

    # clear interior
    for y in range(lowest_corner + 1, lowest_corner + height):
        for x in range(xCoord + 1, xCoord + xSize - 1):
            for z in range(zCoord + 1, zCoord + zSize - 1):
                util.setBlockBatched(x, y, z, "air")

    # roof
    for x in range(xCoord, xCoord + xSize):
        for z in range(zCoord, zCoord + zSize):
            util.setBlockBatched(x, lowest_corner + height, z, blockMaterial)

def buildDoorFromCoord(xCoord, yCoord, zCoord):
    for y in range(yCoord + 1, yCoord + 2):
        util.setBlockBatched(xCoord, y, zCoord, "air")

    util.setBlockBatched(xCoord, yCoord + 1, zCoord, "oak_door[half=lower]")
    util.setBlockBatched(xCoord, yCoord + 2, zCoord, "oak_door[half=upper]")
    util.setBlockBatched(xCoord, yCoord, zCoord - 1, "red_concrete")
    util.setBlockBatched(xCoord, yCoord + 3, zCoord - 1, "wall_torch[facing=north]")

def setMultipleBlocks(xCoord, yCoord, zCoord, xSize, ySize, zSize, material, orientation):
    if orientation == "":
        for y in range(yCoord, yCoord + ySize):
            for x in range(xCoord, xCoord + xSize):
                for z in range(zCoord, zCoord + zSize):
                    util.setBlockBatched(x, y, z, material)

    else:
        for y in range(yCoord, yCoord + ySize):
            for x in range(xCoord, xCoord + xSize):
                for z in range(zCoord, zCoord + zSize):
                    util.setBlockBatched(x, y, z, f"{material}[facing={orientation}]")




