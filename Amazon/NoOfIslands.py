class Solution:
    def get_num_islands(self,grid, i, j):
        if i >= len(grid) or i < 0 or j >= len(grid[0]) or j < 0 or grid[i][j] == '0' or grid[i][j] == 'v':
            return
       
        grid[i][j] = 'v'

        self.get_num_islands(grid, i+1,j)
        self.get_num_islands(grid ,i,j+1)
        self.get_num_islands(grid ,i,j-1)
        self.get_num_islands(grid, i-1,j)
        
    def numIslands(self,grid: List[List[str]]) -> int:                  
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    result +=1
                    self.get_num_islands(grid, i, j)
                    
        return result
        