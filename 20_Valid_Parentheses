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
IDEA: 

empty string should return True 

an odd length string should return False 

otherwise, 
    append each open char to stack 

    when encountering a closing char, pop from the open stack and see     
    if the closing char of the popped open char matches up with the current char

if there are still contents in the stack after iterating through string, return false, as this implies that there are missing closing brackets



COMPLEXITY: 

time = O(N)
space = O(N)

'''
class Solution:
    def isValid(self, s: str) -> bool:
        
        if s == "": 
            return True 
        
        if len(s) % 2 != 0: 
            return False 
        
        stack = []
        open = ["(", "[", "{"]
        mapping = {"(": ")", "[": "]", "{": "}"}
        
        for i in s: 
            
            if i in open: 
                stack.append(i)
            else:
                if len(stack) == 0: #when s starts with a closing bracket
                    return False 
                elif i != mapping[stack.pop()]: #current closing char should match up with popped char from open  
                    return False 
                
        if len(stack) != 0: #case where stack = ["(", "("]
            return False 
        
        return True
