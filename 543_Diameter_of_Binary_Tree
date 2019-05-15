'''
543. Diameter of Binary Tree
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree 
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.


COMPLEXITY: 

time - O(N), visit every node once
space - O(N), the size of the call stack 

IDEA: 

get depth (number of edges from root the leaf) of root's left child  
get depth of root's right child 

update the answer (path length) by get bigger of the existing path length and the combined path of left and right 

return depth (1 + depth of either left or right (pick the one that's greater))
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        self.answer = 0 
        self.getDepth(root)
        return self.answer
        
    def getDepth(self, node): 
        
        if node is None: 
            return 0 
        
        left = self.getDepth(node.left) #get depth of left node 
        right = self.getDepth(node.right) #get depth of right node 
        self.answer = max(self.answer, left + right) 
        
        return max(left, right) + 1 
