#98. Validate Binary Search Tree
# 将树里的数据放入list，查看是否升序
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        l=[]
        if not root:
            return True
        self.l=l
        self.conv(root)
        for i in range(1,len(l)):
            if l[i]<=l[i-1]:
                return False
        return True
    def conv(self,node):
        if node.left:
            self.conv(node.left)
        self.l.append(node.val)
        if node.right:
            self.conv(node.right)
#Runtime: 52 ms, faster than 74.35% of Python3 online submissions for Validate Binary Search Tree.
#Memory Usage: 16.7 MB, less than 5.42% of Python3 online submissions for Validate Binary Search Tree.