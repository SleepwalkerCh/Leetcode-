# 100. Same Tree
#递归从上到下解决问题
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
#Runtime: 40 ms, faster than 41.75% of Python3 online submissions for Same Tree.
#Memory Usage: 14 MB, less than 5.17% of Python3 online submissions for Same Tree.            
                    