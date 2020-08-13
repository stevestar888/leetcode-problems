"""
https://leetcode.com/problems/peeking-iterator/

Strat:
    Store (cache) the next element we should return, along with if
    we have an additional element to return. Have to ensure we turn
    our iterator into 

Stats: O(n) / linear time, O(n) / linear space
    Runtime: 16 ms, faster than 94.98% of Python online submissions for Peeking Iterator.
    Memory Usage: 12.7 MB, less than 93.31% of Python online submissions for Peeking Iterator.
    
Clean solution by Stefan: https://leetcode.com/problems/peeking-iterator/discuss/72557/NexthasNext-use-peek
"""
class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        #make our vars accessible within whole class by using self
        self.iterator = iterator
        
        #try to init our vars used for caching
        if self.iterator.hasNext():
            self.cached_has_next = True
            self.cached_next = iterator.next()
        else:
            self.cached_has_next = False
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.cached_next
        

    def next(self):
        """
        :rtype: int
        """
        tmp = self.cached_next
        
        #see if we can call next() again
        if self.iterator.hasNext():
            #update cached_next with new element
            self.cached_next = self.iterator.next()
        else:
            self.cached_has_next = False
        
        #return the prev elem which was stored in tmp
        return tmp
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cached_has_next
        

# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].