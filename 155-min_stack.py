"""
https://leetcode.com/problems/min-stack/

Strat:
    The only modification between this problem's requirements and a regular stack
    is that this stack needs to be able to return the minimum element that's currently
    still on the stack. Knowing that returning the element does not remove it from the
    stack, we can cleverly store the "min elem so far" along with the element's actual
    val when we put it on the stack.
    
    As we built the stack up, the self.min attribute will decrease or remain the same,
    because we have more and more elements to choose from.

Stats: O(1) / constant time, O(n) / linear space 
    Runtime: 44 ms, faster than 99.57% of Python online submissions for Min Stack.
    Memory Usage: 17.2 MB, less than 5.20% of Python online submissions for Min Stack.
"""
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = [] #stack structure: [val_of_elem, min_of_stack_so_far]
        self.min_so_far = float('inf') #because we don't have anything in stack
        #if we needed to check whether the stack is non-empty stack for
        #the pop, top and get_min operations... we can have a var self.is_empty

        
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.min_so_far = min(self.min_so_far, x)
        elem = [x, self.min_so_far]
        self.stack.append(elem)
        

    def pop(self):
        """
        :rtype: None
        """
        #actually pop the elem from stack
        self.stack.pop()
        
        #see what self.min_so_far should be now
        if self.stack: #take the elem from top of stack
            self.min_so_far = self.stack[-1][1]
        else: #stack is empty so self.min_so_far is back to inf
            self.min_so_far = float('inf')
        

    def top(self):
        """
        :rtype: int
        """
        #return the val at the top of the stack
        return self.stack[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        #return the minimum number in the stack so far
        return self.stack[-1][1]


"""
Attempt at using the named tuple collection to make the code cleaner... doesn't work
"""
# class MinStack(object):

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         #if we needed to check whether the stack is non-empty stack for
#         #the pop, top and getMin operations... we can have a var self.is_empty
#         self.stack = []
#         self.min = float('inf')
#         self.Stack_Elem = collections.namedtuple('val', 'min_so_far')


#     def push(self, x):
#         """
#         :type x: int
#         :rtype: None
#         """
#         self.min = min(self.min, x)
#         elem = self.Stack_Elem(val=x, min_so_far=self.min)
#         self.stack.append(elem)
        

#     def pop(self):
#         """
#         :rtype: None
#         """
#         #actually pop the elem from stack
#         self.stack.pop()
        
#         #see what self.min should be now
#         if self.stack: #take the elem from top of stack
#             self.min = self.stack[-1].min_so_far
#         else: #stack is empty so self.min is back to inf
#             self.min = float('inf')
        

#     def top(self):
#         """
#         :rtype: int
#         """
#         #return the val at the top of the stack
#         return self.stack[-1].val
        

#     def getMin(self):
#         """
#         :rtype: int
#         """
#         #return the minimum number in the stack so far
#         return self.stack[-1].min_so_far

