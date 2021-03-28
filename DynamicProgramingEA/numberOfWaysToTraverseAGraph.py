def numberOfWaysToTraverseGraph(width, height):
    # Write your code here.

    noOfWays = [[0 for _ in range(width+1)] for _ i in range(height+1)]
    for widthIdx in range(1, width):
        for heightIdx in range(1, height):
            if widthIdx == 1 or heightIdx == 1:
                noOfWays[heightIdx][widthIdx] = 1
            else:
                noOfWaysLeft  = noOfWays[heightIdx][widthIdx-1]
                noOfWaysUp  = noOfWays[heightIdx-1][widthIdx]
                noOfWays[heightIdx][widthIdx] = noOfWaysLeft + noOfWaysUp

    return noOfWays[height][width]

