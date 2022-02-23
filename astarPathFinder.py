"""Methods to compute the path between two blocks"""
from heapq import *


"""___PATH FINDING___"""
# calculate the distance between 2 points (Euclidian distance)
def heuristic(a, b):
    return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2


# astar algorithm to compute the path
def astar(array, start, goal):
    #neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # movements to reach the neighbors, diagonals prohibited
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]  # diagonals allowed

    close_list = set()  # list of positions we do not need to consider again
    came_from = {}  # a dictionary that contains all the paths at each iteration (parents position)
    gscore = {start: 0}  # a dictionary that contains our G score by iteration
    fscore = {start: heuristic(start, goal)}  # a dictionary that contains our F score by iteration
    open_list = []  # list of positions that are being considered

    heappush(open_list, (fscore[start], start))  # pushing the start position and F score onto the open list

    while open_list:  # check for available positions until no more

        current = heappop(open_list)[1]  # extract the smallest item from the heap (with the lowest F score)

        if current == goal:  # extract and return the shortest path if we reached the goal
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            return data

        close_list.add(current)  # otherwise add the current position to the closed list
        # if current is in the closed list then skip also check if the block is valid
        for i, j in neighbors:  # loop through the neighbors
            neighbor = current[0] + i, current[1] + j
            tentative_g_score = gscore[current] + heuristic(current, neighbor)  # calculating the G score
            if 0 <= neighbor[0] < array.shape[0]:  # if zPos authorized
                if 0 <= neighbor[1] < array.shape[1]:  # if xPos authorized
                    if array[neighbor[0]][neighbor[1]] == 1:  # if it is a house
                        continue  # ignore the neighbor and continue
                else:
                    # xPos unauthorized
                    continue
            else:
                # zPos unauthorized
                continue

            if neighbor in close_list and tentative_g_score >= gscore.get(neighbor, 0):
                # if the neighbor is in closed list and the G score is greater than G score for that position ignore it
                continue

            if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1] for i in open_list]:
                # if a new untested position for the neighbor
                came_from[neighbor] = current  # update the came from
                gscore[neighbor] = tentative_g_score  # update the G score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)  # update the F score
                heappush(open_list, (fscore[neighbor], neighbor))  # pushing the position onto the open list

    return False


"""___CALLING METHOD___"""
def computePath(grid, start, goal):
    path = astar(grid, start, goal)
    return path
