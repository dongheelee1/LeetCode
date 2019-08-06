'''
695. Max Area of Island

Medium

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
'''
class Solution:
     
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        
        #check to see if the grid is there 
        if grid is None and len(grid) == 0: 
            return None 
        
        #initialize max 
        maxArea = 0 
        
        #traverse through grid, if you encounter an 'X', get count 
        for i in range(len(grid)): 
            for j in range(len(grid[0])): 
                if grid[i][j] == 1: 
                    #sink the current ship and get the area of the current ship 
                    count = self.sinkAndCount(0, grid, i, j)
                    #calculate the maxArea 
                    maxArea = max(maxArea, count)
        return maxArea 
    
    def sinkAndCount(self, count, grid, i, j): 
        
        grid[i][j] = 0
        count += 1 
        
        if i < len(grid)-1 and grid[i+1][j] == 1:
            count = self.sinkAndCount(count, grid, i+1, j)
        if i > 0 and grid[i-1][j] == 1:
            count = self.sinkAndCount(count, grid, i-1, j)
        if j < len(grid[0])-1 and grid[i][j+1] == 1:
            count = self.sinkAndCount(count, grid, i, j+1)
        if j > 0 and grid[i][j-1] == 1:
            count = self.sinkAndCount(count, grid, i, j-1)
            
        return count 
