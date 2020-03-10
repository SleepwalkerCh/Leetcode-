#110. Balanced Binary Tree
#这种方法不行，是用来算是否为满二叉树的方法
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
        num=0
        self.num=num
        self.calc(root)
        dep=self.depth(root,0)
        print(self.num,dep)
        return not 1<<(dep-1)>self.num
    def calc(self,root):
        if root:
            self.num+=1
            self.calc(root.left)
            self.calc(root.right)
    def depth(self,root,num):
        if root==None:
            return num
        else:
            return max(self.depth(root.left,num+1),self.depth(root.right,num+1))