'''
941. Valid Mountain Array

Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]
 

Example 1:

Input: [2,1]
Output: false
Example 2:

Input: [3,5,5]
Output: false
Example 3:

Input: [0,3,2,1]
Output: true
 

Note:

0 <= A.length <= 10000
0 <= A[i] <= 10000
'''
class Solution:
    
    def validMountainArray(self, A: List[int]) -> bool:
        
        #idea is keep comparing i-th element and i+1-st element 
        
        '''
        keep looping if i is within bounds and i+1-st element is greater than i-th element 
        '''
        if len(A) == 0 or len(A) == 1 or len(A) == 2: 
            return False 
        
        i = 0 
        
        #walk up the mountain 
        while i+1 < len(A) and A[i] < A[i+1]: 
            i += 1 
        
        #peak can't be the first or the last 
        if i == 0 or i == len(A)-1: 
            return False 
        
        #walk down the mountain 
        while i+1 < len(A) and A[i] > A[i+1]:  
            i += 1
        
        return i == len(A) - 1
