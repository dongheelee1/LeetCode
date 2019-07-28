'''
200. Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''
class Solution:
    
    '''
    IDEA: 
    
    numIslands take in a grid and spits back a number, that is the number of isladnds in the grid 
    
    numIslands: 
    
    check if grid is None or is an empty list, then return 0 
    
    otherwise, 
    
    traverse through the grid (this means there is a nested for loop)
    
        if we encounter 0, we don't care 
        
        if we encounter 1, 
            1. we want to traverse its adjacents and sink any if they are equal to 1 (do a dfs that will return 1)
            2. add 1 to numIslands 
        
    return number of islands 
    
    
    DFS (takes in grid, i, j and just sinks any square that is '1') 
    
    sink the square that is 1 (set it to 0)
    traverse left, right, down, up only if they are within bounds and are equal to 1
    
    
    '''
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if grid is None or len(grid) == 0: 
            return 0 
        numberOfIslands = 0 
        for i in range(len(grid)): #row 
            for j in range(len(grid[0])): #column 
                if grid[i][j] == '1': 
                    numberOfIslands += 1 
                    self.dfs(grid, i, j)
        return numberOfIslands 
    
    def dfs(self, grid, i, j): 

        grid[i][j] = '0'
        
        if i+1 < len(grid) and grid[i+1][j] == '1': 
            self.dfs(grid, i+1, j)
        if i-1 > -1 and grid[i-1][j] == '1': 
            self.dfs(grid, i-1, j)
        if j-1 > -1 and grid[i][j-1] == '1':
            self.dfs(grid, i, j-1)
        if j+1 < len(grid[0]) and grid[i][j+1] == '1':
            self.dfs(grid, i, j+1)
