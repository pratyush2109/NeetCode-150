# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, res):
        if root==None:
            return
        
        self.inorder(root.left,res)
        res.append(root.val)
        self.inorder(root.right,res)
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root.left==None and root.right==None and k==1:
            return root.val
        
        res=[]
        self.inorder(root, res)
        return res[k-1]