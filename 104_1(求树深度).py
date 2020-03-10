#104. Maximum Depth of Binary Tree
#递归深搜做法，有点慢？
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root==None:
            return 0
        else:
            return self.depth(root,0)
    def depth(self,root,num):
        if root==None:
            return num
        else:
            return max(self.depth(root.left,num+1),self.depth(root.right,num+1))
#Runtime: 64 ms, faster than 6.89% of Python3 online submissions for Maximum Depth of Binary Tree.
#Memory Usage: 16 MB, less than 12.50% of Python3 online submissions for Maximum Depth of Binary Tree.