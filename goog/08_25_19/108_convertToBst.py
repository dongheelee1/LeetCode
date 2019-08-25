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
Accepted
288,779
Submissions
552,897
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums is None or len(nums) == 0: 
            return None 
        
        return self.convertToBST(nums, 0, len(nums)-1)
        
    def convertToBST(self, nums, left, right):
        
        if left > right: 
            return None 
        
        mid = (left + right) // 2
        curr = TreeNode(nums[mid])
        curr.left = self.convertToBST(nums, left, mid-1)
        curr.right = self.convertToBST(nums, mid+1, right)
        return curr
