'''
520. Detect Capital

Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
 

Example 1:

Input: "USA"
Output: True
 

Example 2:

Input: "FlaG"
Output: False
 

Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
'''
'''
idea: 
go through the word letter by letter and increment count of capitals accordingly 
return the conjunction of 3 conditions 
1. capitals == len(w) 
2. w[0].isupper() and capitals == 1 
3. capitals == 0 
'''
class Solution:
    
    def detectCapitalUse(self, word: str) -> bool:
        
        #conditions? 
        #1. all capital 
        #2. all lowercase 
        #3. first character is lowercase 
        
        #go through the entire word and count the number of capitals
        capitals = 0 
        for i in range(len(word)):
            
            if word[i].isupper(): 
                capitals += 1 
                
        return len(word) == capitals or (capitals == 1 and word[0].isupper()) or capitals == 0 
        
