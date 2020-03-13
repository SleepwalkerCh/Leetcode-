# 144. Binary Tree Preorder Traversal
# 迭代做法 
# 一直遍历左子树直到为空，接着往母树搜寻直到右子树非空进行迭代
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
        stack=[root]
        res=[]
        while stack!=[]:
            
            res.append(stack[-1].val)
            now=stack[-1].left
            while now!=None:
                stack.append(now)
                res.append(now.val)
                now=now.left
            
            while stack!=[]:
                next=stack.pop().right
                if next!=None:
                    stack.append(next)
                    break
        return res
#Runtime: 28 ms, faster than 65.21% of Python3 online submissions for Binary Tree Preorder Traversal.
#Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Binary Tree Preorder Traversal.