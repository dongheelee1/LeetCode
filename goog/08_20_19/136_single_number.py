'''
136. Single Number

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
        
        #since every element appears twice, you can delete the element element in the hashset if you see it again 
        
        hash = {}
        
        for i in nums: 
            
            if i not in hash: 
                
                hash[i] = 1 
                
            else: 
                
                del hash[i]
                
        return list(hash.keys())[0]
