import math
import requests
from utils import interfaceUtils


def getBiome(x, z, dx, dz):
    """**Returns the chunk data.**"""
    x = math.floor(x / 16)
    z = math.floor(z / 16)
    url = f'http://localhost:9000/chunks?x={x}&z={z}&dx={dx}&dz={dz}'
    try:
        response = requests.get(url)
    except ConnectionError:
        return -1
        #return "minecraft:plains"
    #print(response.text)
    biomeData = response.text.split(":")
    #print(biomeId[6])
    biomeInfo = biomeData[6].split(";")
    #print(*biomeInfo)
    biome = biomeInfo[1].split(",")
    #print(*biome)
    biome[0]

    return biome[0]

# get the height at (x, z) position
def heightAt(x, z, heightmap, area):
    """Access height using local coordinates."""
    # Warning:
    # Heightmap coordinates are not equal to world coordinates!
    return heightmap[(x - area[0], z - area[1])]


# set the block at (x, y, z) using batching
def setBlockBatched(x, y, z, block):
    """Place blocks or add them to batch."""
    interfaceUtils.placeBlockBatched(x, y, z, block, 100)


# set the block at (x, y, z) without using batching
def setBlock(x, y, z, block):
    interfaceUtils.setBlock(x, y, z, block)


# check that r1 and r2 do not overlap
def rectanglesOverlap(r1, r2):
    if (r1[0] >= r2[0] + r2[2] + 5) or (r1[0] + r1[2] <= r2[0] - 5) or (r1[1] + r1[3] <= r2[1] - 5) or (r1[1] >= r2[1] + r2[3] + 5):
        return False
    else:
        return True





    



