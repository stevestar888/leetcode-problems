"""
https://leetcode.com/problems/binary-tree-right-side-view/

Stategy: use BFS to find when we have reached the end of a level (this is what the inner for loop does). 
    The last item at a given level is therefore the rightmost element. 
    Alternatively, you can use a counter variable to keep track of when you'll be on the last elem
    of the level, then decrement at the end of each while loop iteration.

Runtime: O(V) or O(n) because it's a modification of BFS
    Runtime: 12 ms, faster than 97.69% of Python online submissions for Binary Tree Right Side View.
    Memory Usage: 12.9 MB, less than 7.14% of Python online submissions for Binary Tree Right Side View.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        queue = deque()
        
        if (root == None):
            return ans
        
        queue.append(root)
        while queue: #have items in the bruce
            # for item in queue:
            for i in xrange(len(queue)):
                item = queue.popleft()
            
                #check if we have left kid
                if (item.left):
                    queue.append(item.left)
                    
                #check if we have right kid
                if (item.right):
                    queue.append(item.right)
            
            ans.append(item.val)
            print(item.val)
        
        return ans

    # no inner BFS for-loop; use counter var instead
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        queue = deque()
        visited = []
        
        #if graph is empty
        if (root == None):
            return ans
        
        #initiate BFS
        queue.append(root)
        counter = len(queue) #keeps track of what level we're on
        
        #begin BFS
        while queue:
            node = queue.popleft()
            visited.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
            
            # if we reached the end of a level, add that level's last node to ans
            # else, reduce the counter by one
            if counter > 0:
                counter -= 1
            if counter == 0: 
                ans.append(visited[-1])
                counter = len(queue)
                
        return ans
            
            
            
