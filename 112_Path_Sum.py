'''
112. Path Sum

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        '''
        COMPLEXITY:
        
        time - O(N) = we visit each node exactly once 
        space - O(N) => worst case (each node in tree has only one child) 
                O(logN) => best case (tree is completely balanced)
        
        IDEA: 
        Base Case: 
        if past the leaf node, return False (there isn't a path from root to leaf)
        
        At each depth i, subtract current value from existing sum and update the sum
        
        If at a leaf node: 
            check to see if updated sum is 0 (there exists a path from root to leaf)
            if it is, return True 
            else, return False 
        
        return hasPathSum on right branch or hasPathSum on left branch 
        '''
        
        if root is None: 
            return False 

        sum = sum - root.val 
          
        if root.right is None and root.left is None: #if at a leaf
            if sum == 0: #path exists, return True 
                return True
            else: 
                return False 
        
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
        
