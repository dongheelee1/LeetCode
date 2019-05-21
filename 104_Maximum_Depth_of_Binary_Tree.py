# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
104_Maximum_Depth_of_Binary_Tree
depth = number of edges from root to some node

IDEA: 
Use a DFS strategy 
if root is None, return 0 depth 
else, compare right and left branch depths and select longer of the two + 1

COMPLEXITY: 
time - O(N), visit N nodes 
space -  

in the worst case, the tree is completely unbalanced, e.g. each node has only left child node, the recursion call would occur N times (the height of the tree), therefore the storage to keep the call stack would be O(N)

in the best case (the tree is completely balanced), the height of the tree would be O(log(N)). Therefore, the space complexity in this case would be O(log(N)). 
'''
class Solution:
    
    def maxDepth(self, root: TreeNode) -> int:
        
        if root == None: 
            return 0 
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
