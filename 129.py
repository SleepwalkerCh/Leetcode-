#129. Sum Root to Leaf Numbers
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.numlist,num=[],0
        if root:
            num=root.val
            self.combineNumbers(root,num)
        else:
            return 0
        sumNumber=0
        for i in self.numlist:
            sumNumber+=i
        return sumNumber
    def combineNumbers(self,root,num):
        if root.left==None and root.right==None:
            self.numlist.append(num)
            return
        if root.left:
            self.combineNumbers(root.left,num*10+root.left.val)
        if root.right:
            self.combineNumbers(root.right,num*10+root.right.val)
        return
#Runtime: 28 ms, faster than 80.64% of Python3 online submissions for Sum Root to Leaf Numbers.
#Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Sum Root to Leaf Numbers.