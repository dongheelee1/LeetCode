'''
1119. Remove Vowels from a String

Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.

 

Example 1:

Input: "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"
Example 2:

Input: "aeiou"
Output: ""
 

Note:

S consists of lowercase English letters only.
1 <= S.length <= 1000
'''
class Solution(object):
    def removeVowels(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        
        res = []
        for char in S: 
            if char not in vowels: 
                res += char 
                
        return ''.join(res)
