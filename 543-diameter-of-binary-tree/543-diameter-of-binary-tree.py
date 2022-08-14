# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root, dia):
        if root==None:
            return 0
        
        lh=self.height(root.left, dia)
        rh=self.height(root.right, dia)
        
        dia[0]=max(dia[0],lh+rh)
        return 1+max(lh,rh)
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dia=[0]
        self.height(root,dia)
        return dia[0]