#102. Binary Tree Level Order Traversal
# 用list形式，队列思想实现
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

        
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root==None:
            return []
        res=[]
        queue=[root]
        while queue:
            res_ins,queue_new=[],[]
            for i in queue:
                res_ins.append(i.val)
                if i.left:
                    queue_new.append(i.left)
                if i.right:
                    queue_new.append(i.right)
            res.append(res_ins[:])
            queue=queue_new[:]
        return res
#Runtime: 44 ms, faster than 50.42% of Python3 online submissions for Binary Tree Level Order Traversal.
#Memory Usage: 14.3 MB, less than 6.45% of Python3 online submissions for Binary Tree Level Order Traversal.       

                
                