# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        if root.left==None and root.right==None:
            return [[root.val]]
        
        stack=[]
        stack.append([root,0])
        res=[]
        
        while stack:
            tmp=stack.pop(0)
            curr=tmp[0]
            level=tmp[1]
            
            if len(res)<=level:
                res.append([curr.val])
            else:
                res[level].append(curr.val)
            if curr.left!=None:
                stack.append([curr.left,level+1])
            if curr.right!=None:
                stack.append([curr.right,level+1])
            
        return res
            