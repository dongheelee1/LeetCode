'''
242_Valid_Anagram
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
    '''
    COMPLEXITY: 
    time - O(nlogn) => sorting takes O(nlogn), comparing the two strings take O(n). Since                          O(nlogn) > O(n), overall time complexity is O(nlogn)
    space - O(n) => sorted makes a copy of the string so it costs O(n)
    '''
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t): 
            return False
        
        if sorted(s) == sorted(t): 
            return True 
        else: 
            return False
