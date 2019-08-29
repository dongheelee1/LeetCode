'''
416. Partition Equal Subset Sum (NON DP) 

Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.
 

Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
 

Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
'''
class Solution(object):
    
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        #get the total sum of nums 
        total = sum(nums)
        
        #if the total sum of nums is not even, then return False 
        if total % 2 != 0: 
            return False 
        
        #want to call a recursive function 
        return self.canPartitionRecurse(nums, 0, 0, total)
        
    def canPartitionRecurse(self, nums, index, curr_sum, total): 
        #idea: build on the the curr_sum 
        #if curr_sum is equal to the total / 2, we return True 
        #if curr_sum goes over total / 2 (we want both partitions to have equal sums) or index (which keeps track of element in nums that we want to either exclude or include in curr_sum)
        
        if curr_sum == total/2: 
            return True 
        
        if curr_sum > total/2 or index >= len(nums): 
            return False
        
        #include element or exclude element  
        return self.canPartitionRecurse(nums, index+1, curr_sum, total) or self.canPartitionRecurse(nums, index+1, curr_sum + nums[index], total)
