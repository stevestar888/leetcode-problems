"""

Runtime: 64 ms, faster than 93.23% of Python online submissions for Flatten Nested List Iterator.
Memory Usage: 18.7 MB, less than 14.55% of Python online submissions for Flatten Nested List Iterator.
"""
class NestedIterator(object):

    def __init__(self, nested_list):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.integers = []
        
        def flatten_helper(nested_list):
            for _list in nested_list:
                if _list.isInteger():
                    self.integers.append(_list.getInteger())
                else:
                    flatten_helper(_list.getList())
        
        flatten_helper(nested_list)
        
        self.curr_index = -1
        self.max_index = len(self.integers) - 1
        
        
    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            self.curr_index += 1
            return self.integers[self.curr_index]
        else:
            raise ValueError("Index out of bounds")
        
    
    def hasNext(self):
        """
        :rtype: bool
        """
        return self.curr_index < self.max_index 

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
