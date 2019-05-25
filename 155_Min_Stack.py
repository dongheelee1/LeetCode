'''
155. Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''
import sys 

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_stack = []
        

    def push(self, x: int) -> None:
        '''
        each element in the stack is a tuple 
        the first position is x
        the second position is the current minimum 
        
        get the current min in the stack 
        if x is smaller than current min, then update current min 
        
        push tuple to the stack
        '''
        curr_min = self.getMin() 
        if curr_min > x: 
            curr_min = x 
        self.min_stack.append((x, curr_min))
        
    
    def pop(self) -> None:
        '''
        if stack is empty, return None 
        
        if stack is not empty: 
            save the top element in the stack 
            pop the last element off the stack 
            return the saved top element 
        '''
        if len(self.min_stack) == 0: 
            return None
        pop = self.top()
        self.min_stack.pop()
        return pop

    def top(self) -> int:
        '''
        if stack is empty, return None
        
        if stack is not empty: 
            return the first position value of the last element in the stack 
        '''
        if len(self.min_stack) == 0: 
            return None 
        return self.min_stack[-1][0]

    def getMin(self) -> int:
        '''
        if stack is empty, return the maxsize (since min element has not been set)
        
        if stack is empty: 
            return the second position value of the last element in the stack
        '''
        if len(self.min_stack) == 0: 
            return sys.maxsize
        return self.min_stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
