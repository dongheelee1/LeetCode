'''
349. Intersection of Two Arrays

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
'''
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        #go through nums1 and add elements to contains set 
        contains = set()
        for element in nums1: 
            if element not in contains: 
                contains.add(element)
        
        intersection = set()
        #go through nums2 and add elements to intersections set if it already exists in contains set
        for element in nums2: 
            if element in contains: 
                intersection.add(element)
