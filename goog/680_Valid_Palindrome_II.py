'''
680. Valid Palindrome II

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
'''
class Solution:
    def validPalindrome(self, s: str) -> bool:
        #pointers at each end 
        i = 0 
        j = len(s) - 1
        
        while i < j: 
            
            #characters at either end don't match up 
            #check to see if (i+1, j) -th characters onwards or (i, j+1) -th characters onwards match up 
            if s[i] != s[j]: 
                
                return self.checkPalindrome(s, i+1, j) or self.checkPalindrome(s, i, j-1)
            
            i += 1 
            j -= 1
        
        return True #at this point, the given string is a perfect palindrome 

        
    def checkPalindrome(self, s, i, j): 

        
        while i < j: 
            
            if s[i] != s[j]: 
                
                return False
            i += 1
            j -= 1
            
        return True 
