# 144. Binary Tree Preorder Traversal
# 递推做法
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root==None:
            return []
        stack=[root]
        res=[]
        while stack!=[]:
            res.append(stack[-1].val)
            if stack[-1].left!=None:
                stack.append(stack[-1].left)

