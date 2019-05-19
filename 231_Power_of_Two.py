'''
231. Power of Two

Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false
'''

           
class Solution:
    
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0: 
            return False 
        if n == 1: 
            return True 
        if n % 2 != 0: 
            return False 
        return self.isPowerOfTwo(n//2)
        
    def isPowerOfTwo_Version2(self, n: int) -> bool:
        
        count = 0 
        
        while n/2>=1:     #while number is divisible by 2
            n = n/2       #update the number
            count += 1    #keep track of number of divisions by 2 
        if n == 1:        #n is divisible by 2
            print('Explanation: 2^{} = {}'.format(count, n))
            return True 
        else: 
            return False
