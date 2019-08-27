'''
268. Missing Number

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
'''
class Solution(object):
    
    def missingNumber(self, nums):
        
        """
        :type nums: List[int]
        :rtype: int
        """
        #get a sum of all numbers from 0 to n 
        
        #get a sum of all numbers in num 
        
        #return the difference 
        sum1 = 0
        for i in range(0, len(nums) + 1): 
            sum1 += i 
            
        sum2 = sum(nums)
        
        return sum1 - sum2
