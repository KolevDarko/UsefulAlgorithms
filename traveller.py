import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
"""

??????????????????????????????
????.....?????????????????????
????#####?????????????????????
????..T..?????????????????????
????.....?????????????????????
????#####?????????????????????
??????????????????????????????
??????????????????????????????
??????????????????????????????
??????????????????????????????

def searchControl(maze):
    for (i, row) in enumerate(maze):
        for (j, block) in enumerate(row):
            if str(block) == "C":
                return (i, j)
    return None

"""

maze = [
"####....##..........",
"####....##..........",
"####.T..##..........",
"####.....#..........",
"####.###.#..........",
"####...........C....",
"####....##..........",]

[200, 200, 200, 1000, 0002, 0002, 0002, 0003, 1000, 1000, 9, 9, 10, 11, 12, 13, 14, 15, 16, 17]
[200, 200, 200, 1000, 0001, 0001, 0001, 0002, 1000, 1000, 8, 8, 10, 11, 12, 13, 14, 15, 16, 15]
[200, 200, 200, 1000, 0001, ---0, 0001, 0002, 1000, 1000, 7, 7, 8, 9, 10, 11, 12, 13, 14, 15]
[200, 200, 200, 1000, 0001, 0001, 0001, 0002, 0003, 1000, 0006, 0006, 8, 9, 10, 11, 12, 13, 14, 14]
[200, 200, 200, 1000, 0007, 1000, 1000, 1000, 0003, 1000, 0005, 0006, 0007, 8, 9, 10, 11, 12, 13, 14]
[200, 200, 200, 1000, 0007, 0006, 0005, 0004, 0004, 0004, 0005, 0006, 0007, 8, 9, 10, 11, 12, 13, 14]
[200, 200, 200, 1000, 0007, 0006, 0005, 0005, 1000, 1000, 0005, 0006, 0007, 8, 9, 10, 11, 12, 13, 14]



# R: number of rows.
# C: number of columns.
# A: number of rounds between the time the alarm countdown is activated and the time the alarm goes off.

def getNeighbours((r, c), maze):
    width = len(maze[0])
    height = len(maze)

    #traverse diagonal
    # deltas = [-1, 0, 1]
    # results = list()
    # for d in deltas:
    #     newr = r + d
    #     if newr >= 0 and newr < height:
    #         for dd in deltas:
    #             newc = c + dd
    #             if newc >= 0 and newc < width:
    #                 results.append((newr, newc, maze[newr][newc]))
    
    #traverse only top bottom left right
    deltas = [-1, 0, 1]
    results = list()
    for d in deltas:
        newr = r + d
        if newr >= 0 and newr < height:
            for dd in deltas:
                if abs(d + dd) == 1:
                    newc = c + dd
                    if newc >= 0 and newc < width:
                        results.append((newr, newc, maze[newr][newc]))

    return results



def calculateDistances(maze):
    
    #define points
    start = (2, 5)
    end = (5, 15)
    
    #define helper arrays
    distances = [[200]*20 for i in range(7)]
    visited = [[False]*20 for i in range(7)]

    #init helper arrays
    distances[start[0]][start[1]] = 0
    visited[start[0]][start[1]] = True
    bucket = list()
    bucket.extend(getNeighbours(start, maze))
    
    while len(bucket) > 0:
        temp = bucket.pop(0)
        if visited[temp[0]][temp[1]]:
            continue
        visited[temp[0]][temp[1]] = True
        if temp[2] == "#":
            distances[temp[0]][temp[1]] = 1000
        else:
            tempNeighbours = getNeighbours((temp[0], temp[1]), maze)
            tempDist = 1500
            while tempNeighbours:
                tempN = tempNeighbours.pop(0)
                if not visited[tempN[0]][tempN[1]]:
                    bucket.append(tempN)
                else:
                    if tempDist > distances[tempN[0]][tempN[1]]:
                        tempDist = distances[tempN[0]][tempN[1]]
            distances[temp[0]][temp[1]] = tempDist + 1
    # for d in distances:
    #     print "\n"
    #     for dd in d:
    #         print "%04d" % dd,
    return distances

#discover the path from the destination to the source
def tracePath(start, destination, distances, maze):
    position = start
    while 1:
        newposition = calcNextPosition(position, getNeighbours(position, maze), distances)
        print "Move:", moveTowards(position, newposition)
        if newposition == destination:
            return
        position = newposition

def calcNextPosition(start, neighbours, distances):
    """
    Finds the neighbour with minimum distance of the starting point
    and returns UP, DOWN, LEFT, RIGHT - action how to go there.
    """
    minDist = 1500
    nextNeighbour = start
    for jack in neighbours:
        if distances[jack[0]][jack[1]] < minDist:
            minDist = distances[jack[0]][jack[1]]
            nextNeighbour = jack
    return nextNeighbour[0], nextNeighbour[1]

def moveTowards(start, end):
    if end[0] < start[0]:
        return "UP"

    if end[0] > start[0]:
        return "DOWN"

    if end[1] < start[1]:
        return "LEFT"
    
    if end[1] > start[1]:
        return "RIGHT"
