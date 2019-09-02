'''
896. Monotonic Array

An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.

 

Example 1:

Input: [1,2,2,3]
Output: true
Example 2:

Input: [6,5,4,4]
Output: true
Example 3:

Input: [1,3,2]
Output: false
Example 4:

Input: [1,2,4,5]
Output: true
Example 5:

Input: [1,1,1]
Output: true
 

Note:

1 <= A.length <= 50000
-100000 <= A[i] <= 100000
'''
class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        #if the array is less than 2 elements, return True 
        if A is None or len(A) < 2: 
            return True 
        
        #By comparing first first and last element, decide if possibly monotone_increasing / monotone_decreasing 
        if A[len(A)-1]  > A[0]: 
            
            monotone_increasing = True 
        else: 
            monotone_increasing = False #implies that arr is possibly monotone_decreasing
        
        i = 0
        
        if monotone_increasing ==True:
            #if ever showing decreasing, return False
            while i + 1 < len(A): 
                if A[i+1] < A[i]: 
                    return False
                i += 1
        else: 
            #if ever showing increasing, return False 
            while i + 1 < len(A): 
                if A[i+1] > A[i]: 
                    return False 
                i += 1
                
        #arr is either monotone increasing or decreasing 
        return True 
