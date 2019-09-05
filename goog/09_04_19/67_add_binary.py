'''
67. Add Binary

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
Accepted
333,248
Submissions
826,051
'''
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        s = []
        i = len(a)-1
        j = len(b)-1 
        carry = 0 
        
        while i>=0 or j>=0: 
            
            sum = carry
            
            if i >= 0: 
                sum += int(a[i])
            
            if j >= 0: 
                sum += int(b[j])
            
            #if sum is 2, then carry is 1
            #if sum is 1, then carry is 0 
            #if sum is 0, then carry is 0

            
            s = [sum%2] + s
            carry =sum/2
            i -= 1 
            j -= 1
        if carry: 
            s = [carry] + s
        
        return ''.join(str(i) for i in s)
