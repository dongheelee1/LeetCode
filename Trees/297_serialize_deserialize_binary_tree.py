297. Serialize and Deserialize Binary Tree

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example: 

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

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
        "[1,2,3,null,null,4,5]"
        
        def helperSerialize(root, res): 
            
            if root is None: 
                res += "None, "
            else: 
                res += str(root.val) + ", "
                res = helperSerialize(root.left, res)
                res = helperSerialize(root.right, res)
            return res 
        res = helperSerialize(root, "")
        return res[:-2]

  

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        def helperDeserialize(l):
            

            if l[0] == "None": 
                l.pop(0)
                return None 

            root = TreeNode(int(l[0])) #make the first value of the list 
            l.pop(0) #pop the first value
            root.left = helperDeserialize(l)
            root.right = helperDeserialize(l)
            return root 
                
        data = data.split(", ")

        root = helperDeserialize(data)

        return root
            

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
