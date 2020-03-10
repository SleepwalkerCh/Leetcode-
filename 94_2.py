#94. Binary Tree Inorder Traversal
#迭代方法 中序遍历 用栈解决
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res=[]
        stack=[]
        now=root
        while root:
            while root:
                stack.append(root)
                root=root.left
            
            now=stack.pop()
            res.append(now.val)
            if now.right:
                root=now.right
        return res
#Runtime: 40 ms, faster than 36.55% of Python3 online submissions for Binary Tree Inorder Traversal.
#Memory Usage: 13.9 MB, less than 6.56% of Python3 online submissions for Binary Tree Inorder Traversal.