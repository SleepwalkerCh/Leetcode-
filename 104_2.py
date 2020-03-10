#104. Maximum Depth of Binary Tree
#宽搜做法，快？
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
        num=0
        queue=[root]
        while queue:
            queue_new=[]
            for i in queue:
                if i.left:
                    queue_new.append(i.left)
                if i.right:
                    queue_new.append(i.right)
            queue=queue_new[:]
            num+=1
        return num
#Runtime: 44 ms, faster than 93.09% of Python3 online submissions for Maximum Depth of Binary Tree.
#Memory Usage: 15.2 MB, less than 90.62% of Python3 online submissions for Maximum Depth of Binary Tree.