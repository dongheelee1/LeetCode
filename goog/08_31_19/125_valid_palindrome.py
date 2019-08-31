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

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        
        s = s.lower()

        i = 0 
        j = len(s) -1 
        
        
        #compare character by character starting from opposite ends 
        
        while i < j: 
            while not s[i].isalnum() and i<j:
                i += 1
            while not s[j].isalnum() and i<j: 
                j -= 1
            if s[i] != s[j] and i<j: 
                return False 
            i += 1 
            j -= 1
        return True 
