'''
404. Sum of Left Leaves

Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root is None: 
            return 0 #this is when tree has only 1 root or we recurse to right and there is nothing
        elif root.left is not None and root.left.left is None and root.left.right is None: #in other words if we encounter a left leaf
            return root.left.val + self.sumOfLeftLeaves(root.right)
        else: 
            return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
