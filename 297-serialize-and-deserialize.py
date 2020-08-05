# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return []
        
        queue = deque()
        queue.append(root)
        result = []
        
        while queue:
            item = queue.popleft()
            
            if item:
                result.append(item.val)
                queue.append(item.left)
                queue.append(item.right)

            else:
                result.append("null")
                
        print(result)
        return result
                
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.elem_ptr = 0
        def get_next_elem():
            # if self.elem_ptr < len(data) - 1:
            self.elem_ptr += 1
            return data[self.elem_ptr]
        
        if len(data) == 0:
            return 
        
        root = TreeNode(data[0])
        
        queue = deque()
        queue.append(root)
        
        while queue and self.elem_ptr < len(data) - 1:
            item = queue.popleft()
            print(item.val)
            
            if item: #item exists, so add its children (even if they are null)
                #add its left child
                item.left = TreeNode(get_next_elem())
                
                #add its right child
                item.right = TreeNode(get_next_elem())
                
                queue.append(item.left)
                queue.append(item.right)

            else: #item doesn't exist, so no need to children; advance elem_ptr
                get_next_elem()
                get_next_elem()
        
        return root
        
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
