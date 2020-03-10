#101. Symmetric Tree
#递归方法速度很快，也很简练
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.sol(root.left,root.right)
    def sol(self,sleft,sright):
        if sleft==None or sright==None:
            return sleft==None and sright==None
        if sleft.val!=sright.val:
            return False
        return self.sol(sleft.left,sright.right) and self.sol(sleft.right,sright.left)
#Runtime: 32 ms, faster than 98.73% of Python3 online submissions for Symmetric Tree.
#Memory Usage: 13.8 MB, less than 5.17% of Python3 online submissions for Symmetric Tree.