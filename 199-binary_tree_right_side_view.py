"""
Given a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.

Stategy: use BFS to find when we have reached the end of a level (this is 
what the inner for loop does). The last item at a given level is therefore
the rightmost element.

Runtime:
    Runtime: 12 ms, faster than 97.69% of Python online submissions for Binary Tree Right Side View.
    Memory Usage: 12.9 MB, less than 7.14% of Python online submissions for Binary Tree Right Side View.
    Runs in O(V) or O(n) because it's a modification of BFS

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        
        if (root == None):
            return ans
        
        queue = []
        queue.append(root)
        
        while (queue): #have items in the bruce
            # for item in queue:
            for i in range(len(queue)):
                item = queue[0]
                del queue[0]
            
                #check if we have left kid
                if (item.left):
                    queue.append(item.left)
                    
                #check if we have right kid
                if (item.right):
                    queue.append(item.right)
            
            ans.append(item.val)
            print(item.val)
        
        return ans
            
            
            
