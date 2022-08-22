# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideViewUtil(self, root, level, maxLevel, res):
        if root==None:
            return
        
        if maxLevel[0]<level:
            res.append(root.val)
            maxLevel[0]=level
        
        self.rightSideViewUtil(root.right, level+1, maxLevel, res)
        self.rightSideViewUtil(root.left, level+1, maxLevel, res)
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        maxLevel=[0]
        res=[]
        self.rightSideViewUtil(root, 1, maxLevel, res)
        return res