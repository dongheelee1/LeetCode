'''
9. Palindrome Number

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
'''


class Solution:

    def isPalindrome(self, x: int) -> bool:

        '''
        TIME COMPLEXITY:

        Used a single for loop, which means a O(n) time complexity

        IDEA:

            if x is negative, return False (reversing -121 is 121- ==> not a palindrome)

            if x is positive,

                str_format = str(x)

                get right most digit of x (updated in every loop)

                look at each char from left to right in str_format

                    if right digit != int(str_format[i]):

                        return False

                return True
        '''

        if x < 0:

            return False

        else:

            str_format = str(x)

            for i in range(0, len(str_format) // 2):

                digit = x % 10

                x = x // 10

                if digit != int(str_format[i]):
                    return False

            return True
