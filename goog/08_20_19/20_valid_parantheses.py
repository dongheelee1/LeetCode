'''
20. Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''
class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) % 2 != 0: 
            return False
        
        stack = []
        
        for char in s: 
            
            if char == ")" or char == "}" or char == "]": 
                
                if len(stack) != 0: 
                    open = stack.pop() 
                    
                    if open == "(": 
                        
                        if char != ")": 
                            return False 
                        
                    elif open == "[": 
                        if char != "]": 
                            return False 
                        
                    else: 
                        if char != "}": 
                            return False 
                else: 
                    return False 
            else: 
                stack.append(char)


        if len(stack) != 0: 
            return False 
        return True 
