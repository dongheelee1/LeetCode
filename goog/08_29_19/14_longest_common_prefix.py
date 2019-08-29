'''
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #if empty strs, then return an empty string 
        if strs == None or len(strs) == 0: 
            return ""
        
        #if length of strs is 1, then just return 1 
        if len(strs) == 1: 
            return strs[0]
        
        longest_common_prefix = strs[0]
        for  i in range(1, len(strs)): 
            
            j = 0 
            current_str = strs[i]
            
            while j < len(current_str) and j < len(longest_common_prefix) and current_str[j] == longest_common_prefix[j]: 
                j += 1 
                
            longest_common_prefix = current_str[:j]
        return longest_common_prefix
