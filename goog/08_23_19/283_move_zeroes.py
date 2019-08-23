'''
283. Move Zeroes
Easy

2276

82

Favorite

Share
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0 
        i = 0 
        while i < len(nums): 
            
            if nums[i] != 0: 
                nums[index] = nums[i]
                index += 1
            i += 1

        while index < len(nums): 
            nums[index] = 0 
            index += 1
        return nums
