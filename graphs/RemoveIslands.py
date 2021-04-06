# without aux array 
# make 2s 1 then later do something 

def removeIslands(matrix):
    # Write your code here.

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            colIsBorder  = if col == 0 or col == len(matrix)-1
            rowIsBorder = if row == 0 or row == len(matrix)-1
            isBorder =  colIsBorder or rowIsBorder

            if not isBorder:
                continue

            if matrix[row][col] != 1:
                continue

            changeOnesConnectedBorderToTwos(row, col, matrix)

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):

            color = matrix[row][col]
            if color == 2:
                matrix[row][col] = 1
            elif color == 1:
                matrix[row][col] = 0

    return matrix

def changeOnesConnectedBorderToTwos(startRow, startCol, matrix):

    stack = [(startRow, startColl)]

    while len(stack) >0:
    
        currentRow , currentCol = stack.pop()
        matrix[currentRow][currentCol] = 2

        neighbors = getNeighbors(currentRow, currentCol, matrix)
        for neighbor in neighbors:
            row , col = neighbor

            if matrix[row][col] != 1:
                continue
            
            stack.append([row, col])

def getNeighbors(row, col, matrix):

    neighbors = []
    numCols = len(matrix)
    numRows = len(matrix[0]])

    if row-1 >=0:   # up
        neighbors.append((row-1, col))
    if row +1 < numRows:  # down
        neighbors.append((row+1, col))
    if col+1 < numCols:   # right
        neighbors.append((row, col+1))
    if col-1 >=0:  # left
        neighbors.append((row, col-1))


    return neighbors

    







    

        

    


            

            

            

    

