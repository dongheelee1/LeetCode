'''
257. Binary Tree Paths

Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        def helper(root, path=[]): 
            
            if root is None: 
                return None
            
            if root.left is None and root.right is None: 
                path += [str(root.val)]
                res.append("->".join(path))
                return None 
            
            if root.left:
                helper(root.left, path + [str(root.val)])
            if root.right: 
                helper(root.right, path + [str(root.val)])
        helper(root)
        return res
