'''
101. Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 

Note:
Bonus points if you could solve it both recursively and iteratively.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def isSymmetric(self, root: TreeNode) -> bool:
        
        #an empty tree is always symmetric 
        if root is None: 
            return True 
        
        #otherwise, if not empty, call isSymmetric2(left, right)
        return self.isSymmetric2(root.left, root.right)
    
    
    def isSymmetric2(self, left, right): 
        
        #if either one 
        if left is None or right is None: 
            return left == right #if both are None, return True  
        
        #Otherwise, check if left and right values are the same. 
        #if not the same, return False 
        if left.val != right.val: 
            return False 
        #recurse on (left.left and right.right) (left.right and right.left) 
        return self.isSymmetric2(left.left, right.right) and self.isSymmetric2(left.right, right.left)
