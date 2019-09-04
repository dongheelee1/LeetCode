'''
11. Container With Most Water
(Works, but exceeds time limit) 

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
Accepted
435,436
Submissions
938,453
'''
class Solution(object):
    def maxArea(self, height):
        
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = -float('inf')
        
        #nested for loop 
        for i in range(0, len(height)): 
            
            for j in range(i+1, len(height)): 
                
                min_height = min(height[i], height[j]) #this is a bound on the area
                max_area = max(max_area, min_height * (j-i))
                
        return max_area

    def maxArea2(self, height):
        
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = -float('inf')
        
        i = 0 
        j = len(height)-1 
        while i < j: 
            min_height = min(height[i], height[j])
            max_area = max(max_area, min_height * (j-i))
            if height[i] < height[j]: 
                i += 1
            else: 
                j -= 1 
        return max_area
