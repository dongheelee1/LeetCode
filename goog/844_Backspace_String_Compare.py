'''
844. Backspace String Compare

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
'''
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        '''
        idea: 
        
        Perform the following procedure for both S and T: 
        
        initialize empty stack 
        keep pushing characters into stack if character is not # 
        if character is #, pop off from stack 
        
        compare elements of Sstack and Tstack 
        
        '''
        
        def getBackspaceList(string): 
            stack = [] 
            for i in range(len(string)): 
                if string[i] != '#': 
                    stack.append(string[i])
                elif len(stack) != 0: 
                    stack.pop() 
            return stack 
        
        Sstack = getBackspaceList(S)
        Tstack = getBackspaceList(T)

        if Sstack == Tstack: 
            return True 
        else: 
            return False
