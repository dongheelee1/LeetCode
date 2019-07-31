'''
389. Find the Difference

Easy

Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.
'''
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        
        '''
        idea: 
        
        go through string s 
        
        set character as key in the hashmap if character doesn't exist and set value as 1 
        otherwise, update character's value as hashmap[character] += 1
        
        
        go through string t 
        
        check to see if character exists as key in hashmap 
        
        if it does, then decrement hashmap[character] -= 1
        
        if it doesn't exist as key or the value is 0 then return the character 
        '''
        
        hashmap = {}
        
        for i in range(len(s)): 
            
            if s[i] in hashmap: 
                
                hashmap[s[i]] += 1
                
            else: 
                
                hashmap[s[i]] = 1
                
        for j in range(len(t)): 
            

            
            if t[j] not in hashmap or hashmap[t[j]] == 0:
                return t[j] 
 
            hashmap[t[j]] -= 1
    
        return ''