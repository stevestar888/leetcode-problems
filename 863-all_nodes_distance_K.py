"""
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/submissions/

Strat: 
    (general)
    Find a way for you to access your parents.
    Do a traversal, treating your parent like a child.

    (specically)
    Use a dictionary to store the parent for every node.
    Use DFS traversal, and add the given node's value once you've hit a distance K.
    
Stats:
    Runtime: 40 ms, faster than 19.83% of Python online submissions for All Nodes Distance K in Binary Tree.
    Memory Usage: 13.1 MB, less than 72.67% of Python online submissions for All Nodes Distance K in Binary Tree.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        result = []
        visited = set()
        target_node = None
        parents = {}
        
        #populates the parents dictionary (in order traversal)
        def find_parents(node):
            if node == None:
                return
            
            if node.left:
                parents[node.left.val] = node
                find_parents(node.left)
            
            if node.right:
                parents[node.right.val] = node
                find_parents(node.right)
        
        
        #find all nodes that are distance K from the starting node
        def dfs(node, visited, travelled, K):
            if node == None or node in visited:
                return
            
            visited.add(node)
            if travelled < K: 
                #haven't reached the target distance yet
                #send recursive calls to both children + parent
                dfs(node.left, visited, travelled + 1, K)
                dfs(node.right, visited, travelled + 1, K)
                dfs(parents.get(node.val), visited, travelled + 1, K)
            if travelled == K: #reached target distance
                result.append(node.val)
                
            
        #find the parents for each node
        find_parents(root)
        
        #find all nodes with distance K to the target node
        dfs(target, visited, 0, K)
        
        return result
