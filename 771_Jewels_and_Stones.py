'''
771. Jewels and Stones

You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.
'''
import collections
class Solution:
    
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        '''
        TIME COMPLEXITY - O(n*m) given that n is length of J and m is length of string S
        
        IDEA: 
        -create a frequency dictionary of the string S
        -for each char in J, add count corresponding to the char to sum 
        
        l = collections.Counter(S)
        
        sum = 0 
        
        for char in J: 
            if char in l: 
                sum += l[char]
        return sum 
        '''
        

                
                
        k = [s in J for s in S] #for each char in S (string), is the char a jewel? 
        return(sum(k))
        #return sum
