'''
53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


'''


class Solution:

    def maxSubArray(self, nums: List[int]) -> int:

        max_so_far = 0
        max_update = 0

        for i in range(0, len(nums)):

            max_update += nums[i]

            if max_update < 0:

                if i == 0:
                    max_so_far = nums[i]
                    max_update = 0

                else:

                    if max_update > max_so_far:  # this implies that max_so_far is negative and running max is negative but current arr element is positive
                        max_so_far = nums[i]
                        max_update = 0
                    else:
                        max_update = 0
            elif max_so_far < max_update:

                max_so_far = max_update

        return max_so_far
