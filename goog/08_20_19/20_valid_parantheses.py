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

'''
Idea: 

If length of the string is not even, then it means that there is a bracket for which there is no match. Therefore, return True. 

If the length of the string is even, then we want to initialize a stack that will contain all the open brackets. 

Now, go through character by character in string. 

In the case that we encounter a closed bracket, we want to check if the stack is empty or not. 
    If the stack has elements inside, pop off the open bracket from the stack and compare it with the closed bracket. 
        If the closed bracket is not corresponding to the open, then we want to return False 
        Otherwise, don't 
    If the stack doesn't have elements inside, we want to return False.
    
After we finish going through the string, check that the stack is empty. 

If it is empty, then return True 
If it is not empty, then there is a bracket for which there is not a match. Return False. 

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
