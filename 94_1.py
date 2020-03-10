#94. Binary Tree Inorder Traversal
#递归方法先试一试
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res=[]
        self.res=res
        self.sol(root)
        return self.res
    def sol(self,root):
        if root.Left!=None:
            self.sol(root.Left)
            self.res.append(root.Left.val)
        self.res.append(root.val)
        if root.Right!=None:
            self.res.append(root.Right.val)
            self.sol(root.Right)