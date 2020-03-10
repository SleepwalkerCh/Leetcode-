#110. Balanced Binary Tree
# 平衡树的判定,使用高度为-1 的节点认定为非平衡节点
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        if self.height(root)>0:
            return True
        else:
            return False
            
    def height(self,root):
        if not root:
            return 0
        r_left=self.height(root.left)
        r_right=self.height(root.right)
        if r_left==-1 or r_right==-1:
            return -1
        if abs(r_left-r_right)>1:
            return -1
        return max(r_left,r_right)+1

#Runtime: 64 ms, faster than 51.73% of Python3 online submissions for Balanced Binary Tree.
#Memory Usage: 18.6 MB, less than 45.71% of Python3 online submissions for Balanced Binary Tree.