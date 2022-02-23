from utils import util


# build a fence around the perimeter
def buildFence(heightmap, area):
    for x in range(area[0], area[0] + area[2]):
        z = area[1]
        y = util.heightAt(x, z, heightmap, area)
        util.setBlockBatched(x, y - 1, z, "cobblestone")
        util.setBlockBatched(x, y, z, "oak_fence")
    for z in range(area[1], area[1] + area[3]):
        x = area[0]
        y = util.heightAt(x, z, heightmap, area)
        util.setBlockBatched(x, y - 1, z, "cobblestone")
        util.setBlockBatched(x, y, z, "oak_fence")
    for x in range(area[0], area[0] + area[2]):
        z = area[1] + area[3] - 1
        y = util.heightAt(x, z, heightmap, area)
        util.setBlockBatched(x, y - 1, z, "cobblestone")
        util.setBlockBatched(x, y, z, "oak_fence")
    for z in range(area[1], area[1] + area[3]):
        x = area[0] + area[2] - 1
        y = util.heightAt(x, z, heightmap, area)
        util.setBlockBatched(x, y - 1, z, "cobblestone")
        util.setBlockBatched(x, y, z, "oak_fence")