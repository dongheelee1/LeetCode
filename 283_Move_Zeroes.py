'''
283. Move Zeroes
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


        
        ''' my solution which is inefficient '''
        '''
        count = 0 
        i = 0 
        
        #want to repeat process inside while loop len(nums) - 1 times
        while count < len(nums):
            #idea is that we want to move everything to the right of 0 one step to the left
            if nums[i] == 0: 
                for j in range(i+1, len(nums)): #dependent on the position of 0 in the nums list
                    nums[j-1] = nums[j] #move element one step to the right 
                nums[len(nums)-1] = 0 
            else: 
                i += 1 #if current element is not 0, increment count i by 1 
            count += 1 
        '''
        
        '''
        Complexity: 
        time - O(N)
        space - O(1)
        '''
        
        #count number of zeroes in original list
        count_zeroes = 0 
        for i in range(0, len(nums)): 
            if nums[i] == 0: 
                count_zeroes += 1
        if count_zeroes <= 0: #if there are no zeroes, just print given "nums"
            print(nums)
        #for element that is not 0, set list[new_idx] = element and increment new_idx
        #follow above step in a for loop 
        new_idx = 0 
        for i in range(0, len(nums)): 
            if nums[i] != 0: 
                nums[new_idx] = nums[i]
                new_idx += 1
        
        #replace last count_zeroes indices as 0 
        nums[len(nums)-count_zeroes:] = [0]*count_zeroes
        print(nums)
