'''
49. Group Anagrams

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''

class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        COMPLEXITY: 
        time complexity: O(N * MlogM) where N is the length of strs and M is the length of the longest string in strs 
        space complexity: O(N * M). In the worst case, each word is a separate anagram and each word has max length M 
        
        IDEA: 
        
        initialize a dictionary 
        then, go through each word in strs list, and sort the word alphabetically 
        if the sorted word doesn't exist as key in dictionary, set as dictionary key and append original word to the list (value to the key)
        if the sorted word exists as key in dictionary, append original word to the list (value)
        return the list of values 
        '''
        dict_map = {}
        
        for word in strs: 
            key = ''.join(sorted(word)) 
            if key not in dict_map: 
                
                dict_map[key] = [word]
                
            else: 
                dict_map[key].append(word)

        return list(dict_map.values())
