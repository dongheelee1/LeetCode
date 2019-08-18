'''
242. Valid Anagram

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''
class Solution:
    
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): 
            return False 
        
        #go through string s and populate char-to-freq 
        hashmap = {}
        
        for char in s: 
            if char not in hashmap: 
                hashmap[char] = 1 
            else: 
                hashmap[char] += 1
                
        #go through string t and if decrement count in hashmap      
        for char in t: 
            if char not in hashmap: 
                return False 
            else: 
                hashmap[char] -= 1
                
                if hashmap[char] < 0: 
                    return False 
        return True 
