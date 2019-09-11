'''
383. Ransom Note

Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
Accepted
123,069
Submissions
242,935
'''
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        hash = {}
        
        for char in magazine: 
            if char not in hash: 
                hash[char] = 1 
            else: 
                hash[char] += 1
                
        for char in ransomNote: 
            if char not in hash:
                return False 
            else: 
                hash[char] -= 1 
                if hash[char] < 0: 
                    return False 
        return True 
