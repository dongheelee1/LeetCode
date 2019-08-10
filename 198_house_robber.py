'''
198. House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        #DP[i] = maximum amount of money that we can rob up to the ith house
        
        #check if nums is valid 
        if nums is None or len(nums) == 0: 
            return 0 
        
        #if there is one house in nums, there is only 1 way to return money
        if len(nums) == 1: 
            return nums[0]
        
        #if there are two houses, return the greater value of the two 
        if len(nums) == 2: 
            return max(nums[0], nums[1])
        
        DP = [0]*(len(nums))
        DP[0] = nums[0] 
        DP[1] = max(nums[0], nums[1])
        #now do a bottom up build-up of DP array starting at 3 houses all the way up to (len(nums)-1)-th house. 

        for i in range(2, len(DP)): 
            DP[i] = max(nums[i] + DP[i-2], DP[i-1]) 
            #robbing the current house + most optimal money byr robbing i-2 house (you can't rob adjacent)
            #robbing the house before the current 
        return DP[len(nums)-1]'''
198. House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        #DP[i] = maximum amount of money that we can rob up to the ith house
        
        #check if nums is valid 
        if nums is None or len(nums) == 0: 
            return 0 
        
        #if there is one house in nums, there is only 1 way to return money
        if len(nums) == 1: 
            return nums[0]
        
        #if there are two houses, return the greater value of the two 
        if len(nums) == 2: 
            return max(nums[0], nums[1])
        
        DP = [0]*(len(nums))
        DP[0] = nums[0] 
        DP[1] = max(nums[0], nums[1])
        #now do a bottom up build-up of DP array starting at 3 houses all the way up to (len(nums)-1)-th house. 

        for i in range(2, len(DP)): 
            DP[i] = max(nums[i] + DP[i-2], DP[i-1]) 
            #robbing the current house + most optimal money byr robbing i-2 house (you can't rob adjacent)
            #robbing the house before the current 
        return DP[len(nums)-1]
