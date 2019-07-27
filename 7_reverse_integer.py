'''
7. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''

class Solution:
    def reverse(self, x: int) -> int:
        
        negative = False 
        
        if x < 0: 
            negative = True 
            #work with positive integer and cast as negative later
            x = x * -1 
        reversed = 0 
        while x > 0: 
            #multiply reversed by 10 and add the right-most digit 
            reversed = reversed * 10 + x % 10 
            
            #pop off the right-most digit 
            x = x // 10 
        
        #take note of the note above 
        if reversed > pow(2, 31): 
            return 0 
        
        #if x is initially negative, turn back reversed to negative 
        if negative is True: 
            reversed = reversed * - 1
        
        return reversed 
