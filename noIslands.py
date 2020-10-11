def main(matrix):
        
    domain_count = max_count = 0
    
    def dfs(matrix, i,j, domain_count, max_count):
        
        if domain_count > max_count:
            max_count = domain_count
            
        if i <0 or j<0 or i>=len(matrix) or j >= len(matrix[0]) or matrix[i][j] != 1:
            return 
        matrix[i][j] = 'Visited'
        domain_count += 1
        dfs(matrix, i ,j+1, domain_count, max_count)
        dfs(matrix, i-1 ,j, domain_count, max_count)
        dfs(matrix, i+1 ,j, domain_count, max_count)
        dfs(matrix, i,j-1, domain_count, max_count)

        return max_count 
    for i in range(len(matrix)):
        
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                max_count = dfs(matrix, i, j, domain_count, max_count)

                    
        
    return max_count

main([[1, 1, 1, 0, 0], [0, 1, 1, 0, 0], [ 0, 0 ,0, 0, 1], [1, 0, 0, 1, 1], [1, 1, 0, 0, 1]])