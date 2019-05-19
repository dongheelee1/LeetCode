# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
617_mergeTrees

Time Complexity: O(n) where n is min numer of nodes from the two given trees 
Space Complexity: O(n) --> worst case is when the tree is skewed (each node has one child); O(logn) --> average case, depth will be O(logn)
'''
class Solution:
    
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        '''
        #Consider 4 cases 
        
        #t1 is None and t2 is None 
            
        #t1 exists and t2 exists
        
        #t1 is None and t2 exists 
        
        #t1 exists and t2 is None
        '''
        if t1 is None and t2 is None: 
            return None 
        if t1 and t2 is None: 
            return t1 
        if t1 is None and t2: 
            return t2 
        if t1 and t2: 
            #sum the values of two nodes 
            t1.val = t1.val + t2.val
        
        #preorder traversal: left -> right -> root
        #bottom-up setting of left and right children 
        #will return 3 (the 1st node of newly updated t1) last
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1 
