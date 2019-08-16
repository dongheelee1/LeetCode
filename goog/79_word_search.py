'''
79. Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        
        #traverse through grid 
        #stop when the board's cell matches the first letter of word 
        #if the letters match, conduct dfs on the cell
        
        for i in range(len(board)): 
            
            for j in range(len(board[0])): 
                
                if board[i][j] == word[0] and self.dfs(board, word, i, j, 0): 
                    
                    #conduct dfs 
                    return True
        return False 
                    
    def dfs(self, board, word, i, j, count):
        
        if count == len(word): 
            return True 
        
        #if we go out of bounds (outside of the grid), we want to stop 
        
        #we also want to stop if the current cell is not equal to whatever letter we are at on the word 
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[count]: 
            return False
        
        temp = board[i][j] #remember the current cell 
        board[i][j] = ' ' #erase the current letter for now so that we don't use it more than once 
        found = self.dfs(board, word, i-1, j, count+1) or self.dfs(board, word, i+1, j, count+1) or self.dfs(board, word, i, j-1, count+1) or self.dfs(board, word, i, j+1, count+1)
        board[i][j] = temp #restore cell to original state
        return found 
