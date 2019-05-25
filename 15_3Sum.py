'''
15. 3Sum
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
class Solution:
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        IDEA: 
        
        find the combinations of 3 numbers, iterate through the list with the first pointer, and then trying to find two extra numbers to sum to 0
        '''
        # Sort the elements  
        nums.sort()
        res = []
        
        # Now fix the first element  
        # one by one and find the 
        # other two elements  
        for i in range(0, len(nums)-2): #need to have space for left and right pointers

            if i > 0 and A[i] == A[i-1]:
                continue
            
            # To find the other two elements, 
            # start two index variables from 
            # two corners of the array and 
            # move them toward each other 
            l = i + 1
            r = len(nums)-1 

            while l < r: 
                
                if( A[i] + A[l] + A[r] == 0): #sum of 3 elements == 0 

                    res.append([A[i], A[l], A[r]]) #append results to res
    
                    #move the left and right pointers to the next different numbers, so we do not get repeating result
                    while l < r and A[l] == A[l+1]: 
                        l += 1
                    while l < r and A[r] == A[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif A[i] + A[l] + A[r] < 0: 
                    l += 1
                else: # A[i] + A[l] + A[r] > sum 
                    r -= 1
        # If we reach here, then 
        # no triplet was found 
        return res
                    
                    
