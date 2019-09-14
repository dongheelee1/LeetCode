'''
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #if the array is empty, then we cannot trap any rain water 
        if len(height) == 0 or height is None: 
            return 0 #this is the height of water 
        
        res = 0 
        level = 0 
        left = 0 
        right = len(height) - 1
        
        
        while left < right:
            
            if height[left] < height[right]: 
                lower = height[left]
                left += 1 
            else: 
                lower = height[right]
                right -= 1 
            print("lower: ", lower)
            level = max(level, lower)
            print("level: ", level)
            res += level - lower
            print("res: ", res)
            print("************")
            
        return res 
