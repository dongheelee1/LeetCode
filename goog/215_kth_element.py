'''
215. Kth Largest Element in an Array

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.
'''


'''
keywords like largest or smallest --> check out heap structure 

idea: 
    push everything in given nums to a min heap 
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        import heapq 
        
        #maintain a heap 
        heapq.heapify(nums)
        
        #pop off everything from the heap satisfying the below condition 
        while len(nums) > k: 
            heapq.heappop(nums)
         
        #after there should be exactly two elements making up the heap 
        #return the first of 
        return heapq.heappop(nums)
