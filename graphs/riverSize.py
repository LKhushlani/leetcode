def dfs(matrix, i ,j, count):
    
    if i < 0 or i>=len(matrix) or j <0 or j >= len(matrix[0]) or matrix[i][j] == 'Visited' or matrix[i][j] == 0:
        return 0 
    matrix[i][j] = 'Visited'

    count = 1+ dfs(matrix, i, j+1,count)+ dfs(matrix, i,j-1, count) + dfs(matrix, i-1,j,count)+  dfs(matrix, i+1,j,count)
    return count

def riverSizes(matrix):
    # Write your code here.
    count = 0
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                count  = 0
                count = dfs(matrix, i, j, count)
                result.append(count)

    return result
