class Solution:
    '''
162. Find Peak Element

Medium

A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.
Note:

Your solution should be in logarithmic complexity.

    IDEA: 
    
    We can leverage binary search. This will be faster than going through linearly because runtime will be logn (we are searching half the elements). Also, given nums is sorted leading up to peak. 
    
    
    '''
    def findPeakElement(self, nums: List[int]) -> int:
        
        #nums = [1, 3, 2, 4]
        
        left = 0 
        right = len(nums) - 1 
        
        #when we return, left and right will be equal in value
        
        while left < right: 
            
            #what is the middle 
            mid = (left + right)//2
            
            if nums[mid] < nums[mid+1]:
                print("right subarray")
                print(nums[mid+1])
                print(nums[right])
                #we want to go to the right subarray 
                left = mid + 1
            else: 
                print("left subarray")
                
                print(nums[left])
                print(nums[mid-1])
                #we want to go to the left subarray 
                right = mid
                
        return right 
    
