# 144. Binary Tree Preorder Traversal
# 树的前序遍历
# 递归做法  
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
        return [root.val]+self.preorderTraversal(root.left)+self.preorderTraversal(root.right)
#Runtime: 28 ms, faster than 65.11% of Python3 online submissions for Binary Tree Preorder Traversal.
#Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Binary Tree Preorder Traversal.