# 230. Kth Smallest Element in a B
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.num=0
        self.k=k
        self.res=0
        self.walk(root)
        return self.res
    def walk(self,root):
        
        if root!=None:
            
            if self.walk(root.left):
                return True
            self.num+=1
            if self.num==self.k:
                self.res=root.val
                return True
            if self.walk(root.right):
                return True
        return False
#Runtime: 52 ms, faster than 57.91% of Python3 online submissions for Kth Smallest Element in a BST.
#Memory Usage: 16.8 MB, less than 98.18% of Python3 online submissions for Kth Smallest Element in a BST.