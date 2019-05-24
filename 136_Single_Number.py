'''
136. Single Number
Easy

2389

91

Favorite

Share
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        d = {}
        
        for i in range(0, len(nums)): 
            if nums[i] not in d: 
                d[nums[i]] = 0
            else: 
                d[nums[i]] += 1
                
        for key, value in d.items(): 
            if value == 0: 
                return key
        
        
        ##easy math version 
        #return 2 * (sum(nums)) - sum(nums)
