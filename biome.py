import math
import requests

biomeNumber = [0]

def getBiomeId():
    return biomeNumber[0]

class Biome:
    """Definition of a Biome"""

    def __init__(self):
        self.biomeId = 0

    def getBiome(self, x, z, dx, dz):
        """**Returns the chunk data.**"""
        #x = math.floor(x / 16)
        #z = math.floor(z / 16)
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

        self.biomeId = biome[0]
        self.setBiomeId()

        return self.biomeId

    def setBiomeId(self):
        biomeNumber.clear()
        biomeNumber.append(self.biomeId)