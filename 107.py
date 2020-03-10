#107. Binary Tree Level Order Traversal II
#用递归思路将102题实现即可完成107题
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root==None:
            return []
        res=[]
        queue=[root]
        self.res=res
        self.level(queue)
        return self.res[1:]

    def level(self,queue):
        if queue:
            new_queue,value=[],[]
            for i in queue:
                if i!=None:
                    value.append(i.val)
                    new_queue.append(i.left)
                    new_queue.append(i.right)
            self.level(new_queue)
            self.res.append(value)
#Runtime: 44 ms, faster than 50.79% of Python3 online submissions for Binary Tree Level Order Traversal II.
#Memory Usage: 14.6 MB, less than 7.41% of Python3 online submissions for Binary Tree Level Order Traversal II.