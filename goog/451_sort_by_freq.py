'''
451. Sort Characters By Frequency
Medium
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
'''
class Solution:
    
    def frequencySort(self, s: str) -> str:
        
        '''
        idea: 
        
        get hashmap of the frequency 
        
        sort the items of the hashmap by value (freq) and then by key (char) 
        
        build string based off of the maxheap 
        '''
        from collections import OrderedDict 
        hashmap = OrderedDict()
        
        for char in s: 
            if char not in hashmap: 
                hashmap[char] = 1
            else: 
                hashmap[char] += 1
                

        hashmap = sorted(hashmap.items(), key=lambda t: (-t[1], t[0]))
        #The negation of x[1] is needed to sort the characters by freq in descending first and sort characters in ascending order
        res = ""
        for item in hashmap: 
            char = item[0]
            freq = item[1]
            while freq > 0: 
                res += char
                freq -= 1
        return res 
