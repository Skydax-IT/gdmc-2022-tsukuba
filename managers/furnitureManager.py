from utils import interfaceUtils, util, structuresUtils


def createFurniture(structureType, furnitureType, constructedRectangle, lowest_corner, setting):
    # castle's furniture
    if structureType == "castle":
        if furnitureType == "chest":
            # right tower chest
            buildChest(constructedRectangle[0] + 3, lowest_corner + 1, constructedRectangle[1] + 11,
                       {'diamond': 10}, "north", "left")
            buildChest(constructedRectangle[0] + 4, lowest_corner + 1, constructedRectangle[1] + 11,
                       {'gold_ingot': 10}, "north", "right")

            # left tower chest
            buildChest(constructedRectangle[0] + 16, lowest_corner + 1, constructedRectangle[1] + 11,
                       {'diamond': 10}, "north", "left")
            buildChest(constructedRectangle[0] + 17, lowest_corner + 1, constructedRectangle[1] + 11,
                       {'gold_ingot': 10}, "north", "right")


        elif furnitureType == "torch&windows":
            # main block torches
            util.setBlockBatched(constructedRectangle[0] + 9, lowest_corner + 1, constructedRectangle[1] + constructedRectangle[3] - 2,
                                 "torch")
            util.setBlockBatched(constructedRectangle[0] + 11, lowest_corner + 1, constructedRectangle[1] + constructedRectangle[3] - 2,
                                 "torch")
            util.setBlockBatched(constructedRectangle[0] + 9, lowest_corner + 1,
                                 constructedRectangle[1] + 1,
                                 "torch")
            util.setBlockBatched(constructedRectangle[0] + 11, lowest_corner + 1,
                                 constructedRectangle[1] + 1,
                                 "torch")
            structuresUtils.setMultipleBlocks(constructedRectangle[0] + 7, lowest_corner + 6,
                                              constructedRectangle[1],
                                              7, 1, 1, "torch", "")

            # right tower torches
            util.setBlockBatched(constructedRectangle[0] + 2, lowest_corner + 1, constructedRectangle[1] + 11,
                                 "torch")
            util.setBlockBatched(constructedRectangle[0] + 5, lowest_corner + 1, constructedRectangle[1] + 11,
                                 "torch")
            structuresUtils.setMultipleBlocks(constructedRectangle[0], lowest_corner + 11, constructedRectangle[1] + 6,
                                              8, 1, 1, "torch", "")

            # left tower torches
            util.setBlockBatched(constructedRectangle[0] + 15, lowest_corner + 1, constructedRectangle[1] + 11,
                                 "torch")
            util.setBlockBatched(constructedRectangle[0] + 18, lowest_corner + 1, constructedRectangle[1] + 11,
                                 "torch")
            structuresUtils.setMultipleBlocks(constructedRectangle[0] + 13, lowest_corner + 11, constructedRectangle[1] + 6,
                                              8, 1, 1, "torch", "")

            # windows
            structuresUtils.setMultipleBlocks(constructedRectangle[0] + 2, lowest_corner + 6,
                                              constructedRectangle[1] + 6, 4, 3, 1, "glass_pane", "")  # right
            structuresUtils.setMultipleBlocks(constructedRectangle[0] + 15, lowest_corner + 6,
                                              constructedRectangle[1] + 6, 4, 3, 1, "glass_pane", "")  # left

        elif furnitureType == "spruce_stairs":
            util.setBlockBatched(constructedRectangle[0] + 10, lowest_corner + 1,
                                 constructedRectangle[1] + constructedRectangle[3] - 2,
                                 f"{furnitureType}[facing={setting}]")

    # church's furniture
    elif structureType == "church":
        if furnitureType == "spruce_stairs":
            if setting == "type1":

                # right sits
                structuresUtils.setMultipleBlocks(constructedRectangle[0] + 2, lowest_corner + 1,
                                                  constructedRectangle[1] + 3, 4, 1, 1, "spruce_stairs", "north")
                structuresUtils.setMultipleBlocks(constructedRectangle[0] + 2, lowest_corner + 1,
                                                  constructedRectangle[1] + 5, 4, 1, 1, "spruce_stairs", "north")
                structuresUtils.setMultipleBlocks(constructedRectangle[0] + 2, lowest_corner + 1,
                                                  constructedRectangle[1] + 7, 4, 1, 1, "spruce_stairs", "north")
                #left sits
                structuresUtils.setMultipleBlocks(constructedRectangle[0] + 8, lowest_corner + 1,
                                                  constructedRectangle[1] + 3, 4, 1, 1, "spruce_stairs", "north")
                structuresUtils.setMultipleBlocks(constructedRectangle[0] + 8, lowest_corner + 1,
                                                  constructedRectangle[1] + 5, 4, 1, 1, "spruce_stairs", "north")
                structuresUtils.setMultipleBlocks(constructedRectangle[0] + 8, lowest_corner + 1,
                                                  constructedRectangle[1] + 7, 4, 1, 1, "spruce_stairs", "north")

                #red carpet
                structuresUtils.setMultipleBlocks(constructedRectangle[0] + 6, lowest_corner,
                                                  constructedRectangle[1], 2, 1, 12, "red_concrete", "")

                #gold blocks
                structuresUtils.setMultipleBlocks(constructedRectangle[0] + 6, lowest_corner + 1,
                                                  constructedRectangle[1] + 12, 2, 1, 1, "gold_block", "")

                #windows
                structuresUtils.setMultipleBlocks(constructedRectangle[0], lowest_corner + 2,
                                                  constructedRectangle[1] + 3, 1, 1, 5, "glass_pane", "")
                structuresUtils.setMultipleBlocks(constructedRectangle[0] + 13, lowest_corner + 2,
                                                  constructedRectangle[1] + 3, 1, 1, 5, "glass_pane", "")

            elif setting == "type2":
                # right sits
                structuresUtils.setMultipleBlocks(constructedRectangle[0] + 2, lowest_corner + 1,
                                                  constructedRectangle[1] + 3, 1, 1, 6, "spruce_stairs", "west")
                structuresUtils.setMultipleBlocks(constructedRectangle[0] + 4, lowest_corner + 1,
                                                  constructedRectangle[1] + 3, 1, 1, 6, "spruce_stairs", "west")

                # left sits
                structuresUtils.setMultipleBlocks(constructedRectangle[0] + 9, lowest_corner + 1,
                                                  constructedRectangle[1] + 3, 1, 1, 6, "spruce_stairs", "east")
                structuresUtils.setMultipleBlocks(constructedRectangle[0] + 11, lowest_corner + 1,
                                                  constructedRectangle[1] + 3, 1, 1, 6, "spruce_stairs", "east")

                # blue carpet
                structuresUtils.setMultipleBlocks(constructedRectangle[0] + 6, lowest_corner,
                                                  constructedRectangle[1], 2, 1, 12, "blue_concrete", "")

                # diamond blocks
                structuresUtils.setMultipleBlocks(constructedRectangle[0] + 6, lowest_corner + 1,
                                                  constructedRectangle[1] + 12, 2, 1, 1, "diamond_block", "")

                # windows
                structuresUtils.setMultipleBlocks(constructedRectangle[0], lowest_corner + 2,
                                                  constructedRectangle[1] + 3, 1, 1, 6, "glass_pane", "")
                structuresUtils.setMultipleBlocks(constructedRectangle[0] + 13, lowest_corner + 2,
                                                  constructedRectangle[1] + 3, 1, 1, 6, "glass_pane", "")
                structuresUtils.setMultipleBlocks(constructedRectangle[0] + 4, lowest_corner + 3,
                                                  constructedRectangle[1] + 13, 6, 1, 1, "glass_pane", "")

            # extended door for both types
            for y in range(lowest_corner + 1, lowest_corner + 2):
                util.setBlockBatched(constructedRectangle[0] + 7, y, constructedRectangle[1], "air")

            util.setBlockBatched(constructedRectangle[0] + 7, lowest_corner + 1, constructedRectangle[1],
                                     "oak_door[half=lower, hinge=right]")
            util.setBlockBatched(constructedRectangle[0] + 7, lowest_corner + 2, constructedRectangle[1],
                                     "oak_door[half=upper, hinge = right]")
            util.setBlockBatched(constructedRectangle[0] + 7, lowest_corner, constructedRectangle[1] - 1,
                                     "red_concrete")
            util.setBlockBatched(constructedRectangle[0] + 7, lowest_corner + 3, constructedRectangle[1] - 1,
                                     "wall_torch[facing=north]")

            # torches
            structuresUtils.setMultipleBlocks(constructedRectangle[0] + 6, lowest_corner + 2,
                                              constructedRectangle[1] + 12, 2, 1, 1, "torch", "")

    # clergy house's furniture
    elif structureType == "clergy_house":
        if furnitureType == "all":
            # bed
            util.setBlockBatched(constructedRectangle[0] + 6, lowest_corner + 1, constructedRectangle[1] + 1,
                                            f"{setting}_bed[facing=east, part=foot]")
            util.setBlockBatched(constructedRectangle[0] + 7, lowest_corner + 1, constructedRectangle[1] + 1,
                                            f"{setting}_bed[facing=east, part=head]")

            # cross
            structuresUtils.setMultipleBlocks(constructedRectangle[0] + 4, lowest_corner, constructedRectangle[1] + 2,
                                              1, 1, 4, f"{setting}_concrete", "")
            structuresUtils.setMultipleBlocks(constructedRectangle[0] + 3, lowest_corner, constructedRectangle[1] + 4,
                                              3, 1, 1, f"{setting}_concrete", "")

            # bookshelf
            structuresUtils.setMultipleBlocks(constructedRectangle[0] + 2, lowest_corner + 1,
                                              constructedRectangle[1] + 7, 1, 2, 1, "bookshelf", "")
            structuresUtils.setMultipleBlocks(constructedRectangle[0] + 6, lowest_corner + 1,
                                              constructedRectangle[1] + 7, 1, 2, 1, "bookshelf", "")

            # torches
            util.setBlockBatched(constructedRectangle[0] + 2, lowest_corner + 3, constructedRectangle[1] + 7, "torch")
            util.setBlockBatched(constructedRectangle[0] + 6, lowest_corner + 3, constructedRectangle[1] + 7, "torch")

            # sits
            structuresUtils.setMultipleBlocks(constructedRectangle[0] + 3, lowest_corner + 1,
                                              constructedRectangle[1] + 7, 3, 1, 1, "spruce_stairs[facing=south]", "")

            #windows
            structuresUtils.setMultipleBlocks(constructedRectangle[0], lowest_corner + 2,
                                              constructedRectangle[1] + 3, 1, 1, 3, "glass_pane", "")
            structuresUtils.setMultipleBlocks(constructedRectangle[0] + 8, lowest_corner + 2,
                                              constructedRectangle[1] + 3, 1, 1, 3, "glass_pane", "")

    elif structureType == "peasant_house":
        if furnitureType == "all":
            if setting == "z_longer":
                # bed (could be a function)
                util.setBlockBatched(constructedRectangle[0] + constructedRectangle[2] - 2, lowest_corner + 1,
                                     constructedRectangle[1] + 1, "brown_bed[facing=east, part=head]")

                util.setBlockBatched(constructedRectangle[0] + constructedRectangle[2] - 3, lowest_corner + 1,
                                     constructedRectangle[1] + 1, "brown_bed[facing=east, part=foot]")

                # windows (could be a function)
                util.setBlockBatched((2 * constructedRectangle[0] + constructedRectangle[2]) / 2, lowest_corner + 2,
                                     constructedRectangle[1], "glass_pane")

                util.setBlockBatched((2 * constructedRectangle[0] + constructedRectangle[2]) / 2, lowest_corner + 2,
                                     constructedRectangle[1] + constructedRectangle[3] - 1, "glass_pane")

                # table
                buildTable((2 * constructedRectangle[0] + constructedRectangle[2]) / 2, lowest_corner,
                           constructedRectangle[1] + constructedRectangle[3] - 3)

                # torch
                util.setBlockBatched((2 * constructedRectangle[0] + constructedRectangle[2]) / 2, lowest_corner + 3,
                                     constructedRectangle[1] + constructedRectangle[3] - 2,
                                     "wall_torch[facing=north]")

            elif setting == "x_longer":
                # bed
                util.setBlockBatched(constructedRectangle[0] + constructedRectangle[2] - 2, lowest_corner + 1,
                                     constructedRectangle[1] + constructedRectangle[3] - 2, "brown_bed[facing=south, part=head]")

                util.setBlockBatched(constructedRectangle[0] + constructedRectangle[2] - 2, lowest_corner + 1,
                                     constructedRectangle[1] + constructedRectangle[3] - 3, "brown_bed[facing=south, part=foot]")

                # windows
                util.setBlockBatched(constructedRectangle[0], lowest_corner + 2,
                                     (2 * constructedRectangle[1] + constructedRectangle[3]) / 2, "glass_pane")

                util.setBlockBatched(constructedRectangle[0] + constructedRectangle[2] - 1, lowest_corner + 2,
                                     (2 * constructedRectangle[1] + constructedRectangle[3]) / 2, "glass_pane")

                # table
                buildTable(constructedRectangle[0] + 2, lowest_corner,
                           (2 * constructedRectangle[1] + constructedRectangle[3]) / 2)

                # torch
                util.setBlockBatched(constructedRectangle[0] + 1, lowest_corner + 3,
                                     (2 * constructedRectangle[1] + constructedRectangle[3]) / 2,
                                     "wall_torch[facing=east]")

    elif structureType == "farm":
        if furnitureType == "all":
            # chest
            buildChest(constructedRectangle[0] + 3, lowest_corner + 1, constructedRectangle[1] + 10,
                       {'wooden_hoe': 1}, "north", "right")

            # torch
            util.setBlockBatched(constructedRectangle[0] + 3, lowest_corner + 2, constructedRectangle[1] + 10,
                                 f"wall_torch[facing={setting}]")


def buildChest(x, y, z, itemsCollection, orientation, chestType):
    util.setBlockBatched(x, y, z, f"chest[facing={orientation}, type={chestType}]")
    interfaceUtils.sendBlocks()
    keys_list = list(itemsCollection)
    for i in range(len(keys_list)):
        addChestItem(x, y, z, keys_list[i], itemsCollection[keys_list[i]])


def addChestItem(x, y, z, item, number):
    command = f"replaceitem block {x} {y} {z} container.0 minecraft:{item} {number}"
    interfaceUtils.runCommand(command)

def buildTable(x, lowest_corner, z):
    util.setBlockBatched(x, lowest_corner + 1, z, "oak_fence")
    util.setBlockBatched(x, lowest_corner + 2, z, "oak_pressure_plate")
