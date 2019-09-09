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
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        '''
        look through the grid 
        if we ever find the first letter of the word, we need to start a DFS on the current cell of the board
        '''
        
        for i in range(len(board)): 
            
            for j in range(len(board[0])): 
                
                #check word
                if word[0] == board[i][j]: 
                    
                    if self.dfs(board, i, j, word, 0): 
                        return True 
        return False 
                 

                
    def dfs(self, board, i, j, word, count): 
        
        if count == len(word): 
            return True 
        print(i)
        print(j)
        #if we go outside of bounds or characters don't match, we must return False 
        if i < 0 or i > len(board)-1 or j < 0 or j > len(board[0])-1 or board[i][j] != word[count]: 
            return False 

        temp = board[i][j] #remember the current cell 
        board[i][j] = ' '    
        found = self.dfs(board, i-1, j, word, count+1) or self.dfs(board, i, j+1, word, count+1) or self.dfs(board, i+1, j, word, count+1) or self.dfs(board, i, j-1, word, count+1)
        board[i][j] = temp
        return found 
