'''
763. Partition Labels

A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
Note:

S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.
'''
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        #idea of partition labels 
        
        #for each character, find the last index of the repeating character 
        
        if len(S) == 0: 
            return [0]
        
        d = {ch : i for i, ch in enumerate(S)}
        
        i, j = 0, 0
        res = []
        
        while i < len(S):
            curr_char = S[i]
            end_idx = d[curr_char] if d[curr_char] > i else i
            k = i + 1
            while k < end_idx:
                if d[S[k]] > end_idx:
                    end_idx = d[S[k]]
                k += 1
            res.append(end_idx - i + 1)
            i = end_idx+1
        return res
