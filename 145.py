# 145. Binary Tree Postorder Traversal
# 定义一个二维list，记录当前栈节点状态，如 左子树已入过栈

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack=[[root,0]]
        res=[]
        while stack:
            #print(stack[-1][0].val)
            if stack[-1][1]==0:
                stack[-1][1]=1
                if stack[-1][0].left:
                    stack.append([stack[-1][0].left,0])
                continue
            if stack[-1][1]==1:
                stack[-1][1]=2
                if stack[-1][0].right:
                    stack.append([stack[-1][0].right,0])
            if stack[-1][1]==2:
                res.append((stack.pop())[0].val)
        return res
#Runtime: 20 ms, faster than 96.95% of Python3 online submissions for Binary Tree Postorder Traversal.
#Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Binary Tree Postorder Traversal.