'''
108. Convert Sorted Array to Binary Search Tree

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
IDEA: 

2 functions: 
- sortedArrayToBST (takes in an int array and spits out a BST of type TreeNode) 
- createBST (takes in an int array from sortedArrayToBST and spits out a BST of type TreeNod) 

sortedArrayToBST
- check if int array passed is not None and length != 0 
- otherwise, call createBST that will return a BST 

createBST 
- if past the leaves, return None 
- create root 
- obtain root.left and root.right using recursion 
- return root 
'''
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        #edge case...when nums is None or length of nums is 0, return empty tree
        if nums is None or len(nums) == 0: 
            return None 
        
        return self.createBST(nums, 0, len(nums)-1)
    
    def createBST(self, nums: List[int], left: int, right: int) -> TreeNode 
        
        if left > right: #past the leaf Node 
            return None 
            
        #since the array is sorted, the middle value becomes the root 
        #repeat this for the left subtree and the right subtree 
        
        mid = (left + right)//2
        
        root = TreeNode(nums[mid])
        root.left = self.createBST(nums, left, mid-1)
        root.right = self.createBST(nums, mid+1, right)
        
        return root 
