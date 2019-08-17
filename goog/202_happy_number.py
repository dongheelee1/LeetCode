'''
202. Happy Number

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''
class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = [] #old is used to keep track of sum, if sum is repeated then we have a cycle and know that there is no happy number (a number whose digits squared is equal to 1)   
        sum = n 
        while True:
            s = str(sum)
            sum = 0
            #calculate the squared sum 
            for digit in s:
                sum += int(digit) ** 2

                
            #if the squared sum is equal to 1, then we have our happy number 
            if sum == 1:
                return True
            
            #if we have never seen the sum before, add it to old 
            if sum not in seen:
                seen.append(sum)
            else:
                #we have seen it already so there's a cycle (no happy number)
                return False
