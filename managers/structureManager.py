import structures.castle
import structures.church
import structures.clergy_house
import structures.farm
import structures.peasant_house

from utils import util
from structures.door import Door
import biome


structuresList = []

def getstructuresList():
    return structuresList


class Structure:
    """Definition of a Structure"""

    def __init__(self, structureType):
        self.structureType = structureType
        self.rectangle = (0, 0, 0, 0)
        self.constructedRectangle = (0, 0, 0, 0)
        self.lowest_corner = 0
        self.height = 0
        self.door = Door()

    def pickRectangle(self, area, houses):
        overlapsExisting = True
        while overlapsExisting:
            # pick random rectangle to place new house
            if self.structureType == "church":
                houseRect = structures.church.pickRectangleChurch(area)
            if self.structureType == "castle":
                houseRect = structures.castle.pickRectangleCastle(area)
            if self.structureType == "peasant_house":
                houseRect = structures.peasant_house.pickRectanglePeasantHouse(area)
            if self.structureType == "clergy_house":
                houseRect = structures.clergy_house.pickRectangleClergyHouse(area)
            if self.structureType == "farm":
                houseRect = structures.farm.pickRectangleFarm(area)
            # if self.structureType == "query":
                # houseRect = structures.query.pickRectangleQuery(area)

            self.rectangle = houseRect
            overlapsExisting = self.overlapsChecker(houses)

    def buildStructure(self, doorsList, houses, heightmap, area):
        self.pickRectangle(area, houses)
        self.constructedRectangle = (self.rectangle[0] + 1, self.rectangle[1] + 1, self.rectangle[2] - 2, self.rectangle[3] - 2)
        print(
            f"building {self.structureType} at {self.constructedRectangle[0]}, {self.constructedRectangle[1]} with size {self.constructedRectangle[2]},{self.constructedRectangle[3]}")
        self.getHeight(heightmap, area)
        self.fillTheTerrain(heightmap, area)

        if self.structureType == "church":
            self.height = 6
            self.door = structures.church.buildChurch(self.rectangle, self.constructedRectangle, self.lowest_corner, self.height, doorsList)
        if self.structureType == "castle":
            self.height = 10
            self.door = structures.castle.buildCastle(self.rectangle, self.constructedRectangle, self.lowest_corner, self.height, doorsList)
        if self.structureType == "peasant_house":
            self.height = 4
            self.door = structures.peasant_house.buildPeasantHouse(self.rectangle, self.constructedRectangle, self.lowest_corner, self.height, doorsList)
        if self.structureType == "clergy_house":
            self.height = 4
            self.door = structures.clergy_house.buildClergyHouse(self.rectangle, self.constructedRectangle, self.lowest_corner, self.height, doorsList)
        if self.structureType == "farm":
            self.height = 5
            self.door = structures.farm.buildFarm(self.rectangle, self.constructedRectangle, self.lowest_corner, self.height, doorsList)

        doorsList.append(self.door)

        self.updateStructuresList()

    def updateStructuresList(self):
        structuresList.append(self)

    # check whether there are any overlaps with current houses
    def overlapsChecker(self, houses):
        overlapsExisting = False
        for house in houses:
            if util.rectanglesOverlap(self.rectangle, house):
                overlapsExisting = True
                break
        return overlapsExisting

    def getHeight(self, heightmap, area):
        # find the lowest corner of the house and give it a random height
        self.lowest_corner = max(
            util.heightAt(self.constructedRectangle[0], self.constructedRectangle[1], heightmap, area),
            util.heightAt(self.constructedRectangle[0] + self.constructedRectangle[2] - 1, self.constructedRectangle[1], heightmap, area),
            util.heightAt(self.constructedRectangle[0], self.constructedRectangle[1] + self.constructedRectangle[3] - 1, heightmap, area),
            util.heightAt(self.constructedRectangle[0] + self.constructedRectangle[2] - 1, self.constructedRectangle[1] + self.constructedRectangle[3] - 1, heightmap, area)
        ) - 1

    def fillTheTerrain(self, heightmap, area):
        biomeId = biome.getBiomeId()
        for x in range(self.rectangle[0], self.rectangle[0] + self.rectangle[2]):
            for z in range(self.rectangle[1], self.rectangle[1] + self.rectangle[3]):
                height = util.heightAt(x, z, heightmap, area)
                for y in range(height, self.lowest_corner):
                    if biomeId in ["2", "17", "130"]:
                        util.setBlockBatched(x, y, z, "sand")
                    else:
                        util.setBlockBatched(x, y, z, "dirt")




