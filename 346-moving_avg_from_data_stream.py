"""
https://leetcode.com/problems/moving-average-from-data-stream/

Strat:
    Use a deque.

Stats: O(1) / constant time, O(n) / linear space 
    Runtime: 56 ms, faster than 71.07% of Python online submissions for Moving Average from Data Stream.
    Memory Usage: 16.9 MB, less than 22.42% of Python online submissions for Moving Average from Data Stream.

"""
from collections import deque

class MovingAverage(object):
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.window = deque()
        self.MAX_SIZE = size
        self.count = 0
        self.sum = 0.0
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        #add new item to the window
        self.window.append(val)
        
        #pop first item from queue if we've filled window to capacity
        if self.count >= self.MAX_SIZE:
            self.sum -= self.window.popleft()
        
        #increase sum & count
        self.sum += val
        self.count += 1
        
        #denom is either current count or MAX_SIZE
        return self.sum / min(self.count, self.MAX_SIZE)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)