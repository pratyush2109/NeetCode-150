# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, ans, maximum):
        if root==None:
            return
        
        if root.val>=maximum:
            ans[0]+=1
            maximum=root.val
            
        self.dfs(root.right, ans, maximum)
        self.dfs(root.left, ans, maximum)
    
    def goodNodes(self, root: TreeNode) -> int:
        ans=[0]
        self.dfs(root, ans, -99999)
        return ans[0]