# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def preorder(self, root, l):
        if root==None:
            l.append("N")
            return
        
        l.append(str(root.val))
        self.preorder(root.left, l)
        self.preorder(root.right, l)
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        l=[]
        self.preorder(root, l)
        res=",".join(l)
        return res
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        l=data.split(",")
        self.i=0
        
        def dfs():
            if l[self.i]=="N":
                self.i+=1
                return None
            
            node = TreeNode(int(l[self.i]))
            self.i+=1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()
            

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))