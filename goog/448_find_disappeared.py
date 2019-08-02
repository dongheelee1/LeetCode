'''
448. Find All Numbers Disappeared in an Array

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
'''
class Solution:
    
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        numbers_hashmap = {}
        missing = []
        
        #go through the given nums array and add each element as key in numbers_hashmap if it is not alread
        for i in range(len(nums)): 
            
            if nums[i] not in numbers_hashmap: 
                numbers_hashmap[nums[i]] = 1
        
        #start at 1 and iterate up to length of nums and if j does not exist is key in numbers_hashmap, appending to missing array 
        for j in range(1, len(nums)+1): 
            
            if j not in numbers_hashmap: 
                missing.append(j)
                
        return missing 
