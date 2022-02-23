def findClosestDoor(x, z, doorsList):
    doorsList.sort(key=lambda d: (d.x - x) ** 2 + (d.z - z) ** 2)
    closestDoor = doorsList[0]

    return closestDoor


def getSortedList(doorsList):
    doorsList.sort(key=lambda x: x.x)
    openList = doorsList.copy()
    sortedList = []
    currentDoor = doorsList[0]

    openList.remove(currentDoor)
    sortedList.append(currentDoor)

    while len(sortedList) < len(doorsList):
        nextDoor = findClosestDoor(currentDoor.x, currentDoor.z, openList)
        openList.remove(nextDoor)
        sortedList.append(nextDoor)
        currentDoor = nextDoor
    """for d in doorsList:
        print(d.name)
    for d in sortedList:
        print("\n Sorted", d.name)"""

    return sortedList


class Door:
    """Definition of door"""

    def createDoor(self, x, y, z, list):
        self.name = f"door{len(list)}"
        self.x = x
        self.y = y
        self.z = z

