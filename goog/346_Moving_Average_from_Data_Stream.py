'''
346. Moving Average from Data Stream

Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
'''
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        
        #size = number of elements to divide by 
        self.queue = []
        self.maxSize = size 
        self.sum = 0
        
        

    def next(self, val: int) -> float:
        
        if self.maxSize == len(self.queue): 
            v = self.queue.pop(0)
            self.sum -= v
        
        self.queue.append(val)
        self.sum += val 
        print(val, self.sum)
        return self.sum/len(self.queue)
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
