"""
https://leetcode.com/problems/validate-stack-sequences/submissions/

The greedy solution works by pushing 1 item at a time, and then trying to pop as many as feasible.
"""


class Solution(object):
    """
    Recursive attempt at solving; not sure why it doesn't work.
    """
#     def validateStackSequences(self, pushed, popped):
#         """
#         :type pushed: List[int]
#         :type popped: List[int]
#         :rtype: bool
#         """
#         def recurse(pushed_idx, popped_idx, stack):
#             # base case
#             if pushed_idx == popped_idx == len(pushed) and stack == []:
#                 return True

#             # recursive case
#             # can push?
#             if pushed_idx < len(pushed):
#                 new_stack = stack + [pushed[pushed_idx]]
#                 recurse(pushed_idx + 1, popped_idx, new_stack)

#             # can pop?
#             if popped_idx < len(popped) and stack:
#                 if stack[-1] == popped[popped_idx]:
#                     stack.pop()
#                     recurse(pushed_idx, popped_idx + 1, stack)
        
        
#         return recurse(0, 0, [])
    
    """
    Greedy -- inspired by the real solution
    """
    def validateStackSequences(self, pushed, popped):
        stack = []
        popped_idx = 0
        
        for pushed_item in pushed:
            # push item
            stack.append(pushed_item)
            
            # can pop?
            # conditions: stack has item, popped still has item left, popped has right elem
            while popped_idx < len(popped) and stack and stack[-1] == popped[popped_idx]:
                stack.pop()
                popped_idx += 1
            
        return stack == []
    
#     """
#     Amazing solution!
#     """
#     def validateStackSequences(self, pushed, popped):
#         lenP, i, j, s = len(pushed), 0, 0, 0
#         while i < lenP:
#             if ~s and popped[j] == pushed[s]:
#                 j += 1
#                 s -= 1
#             else:
#                 s += 1
#                 i += 1
#                 if i < lenP: pushed[s] = pushed[i]
#         return not s
            