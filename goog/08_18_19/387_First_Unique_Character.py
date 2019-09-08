'''  
387. First Unique Character in a String

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''  
class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        hash = {}
        
        #get a char: frequency for the string s 
        for char in s: 
            if char not in hash: 
                hash[char] = 1 
            else: 
                hash[char] += 1
        
        #go through the string s and return 
        for idx, value in enumerate(s): 
            if hash[value] == 1: 
                return idx
        return -1
            
