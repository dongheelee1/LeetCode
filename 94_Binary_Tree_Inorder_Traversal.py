# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''
    94. Binary Tree Inorder Traversal
    IDEA: 
    
    do an inorder traversal on binary tree
    
    if node is None, return [] 
    if node is hit, append to the list that is initialized in __init__
    
    
    COMPLEXITY: 
    Time - O(N)
    Space - O(N) in worst case, O(logN) in average case
    '''
    def __init__(self): 
        self.output = []
        
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        if root is None: 
            return []
        
        self.inorderTraversal(root.left)
        self.output.append(root.val)
        self.inorderTraversal(root.right)
        
        return self.output
