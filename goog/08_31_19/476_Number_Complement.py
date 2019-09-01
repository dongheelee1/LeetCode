'''
476. Number Complement

Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
Accepted
113,711
Submissions
181,459
'''
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        result = 0 
        power = 1 
        
        print("result", result)
        print("power", power)
        print("num: ", num)

        print("***************")
        while num > 0: #chip off bit by bit in num from right to left 
            '''
            idea is that we want to  go through bit by bit from right to left
            each bit we want to focus on is given by num % 2....the right most digit
            we want to complement this with 1. For example if the bit is 0, xor this by 1 to get complement 0
            to get the result multiply the either the complement with the current power 
            
            say num is 1011 (or 11 in decimal)
            
            in the second iteration, we will deal with num = 101 
            in the third itertation, we will deal with num = 10 
            in the 4th iteration, we will deal with num = 1 
            
            result is the decimal total of the complement 
            
            in the first iteration 
            '''
            print(bin(num))
            print(bin(num%2))
            #get the last bit --> num%2 gives whatever the remainder is, 0 if even num or 1 if odd num 
            #xor the last bit by 1 to get the complement of the bit --> 0 ^ 1 = 1, 1 ^ 1 = 1
            #multiply by the power and add to result to get the current decimal value
            
            result += (num % 2 ^ 1) * power  #10 ^ 1 => 10*2
            print("result: ", result)
            
            #keep track of the power
            power <<= 1 # A single left shift multiplies a binary number by 2
            print("power", power)
            num >>= 1 #divides a number by 2, throwing out any remainders/last bit 
            print("num", num)
            print("***************")
            
        return result
