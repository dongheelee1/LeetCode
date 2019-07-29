'''
219. Contains Duplicate II

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        
        idea: 
        
        maintain a hashmap [key is the item and value is the index]
        
        go through the arr 
        
        if current number is a key in the hashmap 
            get the corresponding value (index) of the key 
                check to see if current index - key's value is at most k 
                    if so, 
                        return True 
                    else
                        update index corresponding to key to i 
        else: 
            hashmap[current number] = current index 
            
        return False 
        '''
        
        hashmap = {}
        
        for i in range(len(nums)): 
            
            if nums[i] in hashmap: 
                
                diff = i - hashmap[nums[i]]
                
                if diff <= k: 
                    return True
                else: 
                    hashmap[nums[i]] = i
            else: 
                
                hashmap[nums[i]] = i 
        return False 
