#  199. Binary Tree Right Side View
# 宽搜思路逐个遍历，效率可能不够高
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
        old=[root]
        res=[root.val]
        while old!=[]:
            new=[]
            for i in old:
                if i.left:
                    new.append(i.left)
                if i.right:
                    new.append(i.right)
            if new!=[]:
                res.append(new[-1].val)
            
            old[:]=new[:]
        return res
#Runtime: 20 ms, faster than 99.17% of Python3 online submissions for Binary Tree Right Side View.
#Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Binary Tree Right Side View.