'''
169. Majority Element

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
'''

'''
construct a hashmap consisting of character: count 
--> for loop going through the string 

go through the hashmap 
if value (count) of the current key (character) is greater than n/2, return the character 
'''
class Solution:
    
    def majorityElement(self, nums: List[int]) -> int:
        
        hashmap = {}
        
        for i in range(len(nums)): 
            
            if nums[i] not in hashmap: 
                
                hashmap[nums[i]] = 1 
            else: 
                
                hashmap[nums[i]] += 1
        

        for key in hashmap: 

            if hashmap[key] > len(nums)/2: 
                
                return key
