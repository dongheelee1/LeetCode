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
        #initially set monotoneDecreasing to True, monotoneIncreasing to False 
        
        monotoneDecreasing = True 
        monotoneIncreasing = True 
        
        for i in range(0, len(A)-1):
        
            #if you encounter increasing (monotoneDecreasing --> False, monotoneIncreasing stay the same)
            #if you encounter decreasing (monotoneDecreasing stay the same, monotoneIncreasing --> False)
            #if both increasing and decreasing at the same time, then we know it's not monotone increasing or decreasing 
            if A[i] < A[i+1]: 
                monotoneDecreasing = False
            if A[i] > A[i+1]:  
                monotoneIncreasing = False 
        return monotoneDecreasing or monotoneIncreasing
