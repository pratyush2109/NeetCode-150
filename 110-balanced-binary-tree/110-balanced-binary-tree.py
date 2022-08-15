# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self,root):
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return 1
        
        return 1+max(self.height(root.left),self.height(root.right))
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return True
        if root.left!=None:
            lh=self.height(root.left)
        else:
            lh=0
        if root.right!=None:
            rh=self.height(root.right)
        else:
            rh=0
            
        if abs(lh-rh)<=1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        else:
            return False