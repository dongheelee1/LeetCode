'''
125. Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:

        if s == "": 
            return True
        
        import string
        alphanumeric = list(str(i) for i in range(10)) + list(string.ascii_lowercase)

        s = s.lower()

        i = 0 
        j = len(s) - 1 

        while i < j: 

            while s[i] not in alphanumeric and i<j: 
                i += 1 
            while s[j] not in alphanumeric and i<j: 
                j -= 1

            if s[i] != s[j] and i < j: 
                return False 
        
            i += 1 
            j -= 1
            
        return True 
