'''
Serialization is the process of converting a data structure or object into a sequence of bits so that it 
can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed 
later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your 
serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be 
serialized to a string and this string can be deserialized to the original tree structure.

Example: 

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not 
necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize 
algorithms should be stateless.
'''
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = []
        if not root: return result
        
        que = deque([root])
        while que:
            current = que.popleft()
            result.append(current.val if current else None)
            if current:
                que.append(current.left)
                que.append(current.right)
        
        while result and result[-1] is None: result.pop()

        return result 
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        root = TreeNode(data[0])
        nodeQueue = [root]
        front, start = 0, 1
        while start < len(data):
            node = nodeQueue[front]
            front = front + 1

            if data[start] is not None:
                node.left = TreeNode(data[start])
                nodeQueue.append(node.left)
            
            start += 1
            if start >= len(data): break

            if data[start] is not None:
                node.right = TreeNode(data[start])
                nodeQueue.append(node.right)
        
            start += 1
        
        return root