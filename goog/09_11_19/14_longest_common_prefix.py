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
        if strs is None or len(strs) == 0: 
            return ""
        
        common = strs[0]
        
        for i in range(1, len(strs)):
            
            current = strs[i]
            k = 0 
            
            while k < len(common) and k < len(current) and common[k] == current[k]: 
                k += 1
                
            common = common[:k]
            
        return common
