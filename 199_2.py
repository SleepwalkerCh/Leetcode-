#  199. Binary Tree Right Side View
# 递归思路
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root==None:
            return []
        left=self.rightSideView(root.left)
        right=self.rightSideView(root.right)
        return [root.val]+right+left[len(right):]
#Runtime: 16 ms, faster than 99.83% of Python3 online submissions for Binary Tree Right Side View.
#Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Binary Tree Right Side View
