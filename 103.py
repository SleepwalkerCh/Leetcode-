#103. Binary Tree Zigzag Level Order Traversal
#用栈结构，判断奇偶左右不同处理
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root==None:
            return []
        res=[]
        queue=[root]
        num=0
        while queue:
            res_ins,queue_new=[],[]
            while queue:
                i=queue.pop()
                res_ins.append(i.val)
                if num%2==0:
                    if i.left:
                        queue_new.append(i.left)
                    if i.right:
                        queue_new.append(i.right)
                else:
                    if i.right:
                        queue_new.append(i.right)
                    if i.left:
                        queue_new.append(i.left)
            num+=1    
            res.append(res_ins[:])
            queue=queue_new[:]
        return res
#Runtime: 32 ms, faster than 97.42% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
#Memory Usage: 13.9 MB, less than 5.41% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.