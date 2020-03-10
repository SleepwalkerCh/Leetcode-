#95. Unique Binary Search Trees II
#该解法较深的增强了对递归的认识
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n: int):
        res=[]
        return self.solve(1,n+1)
    def solve(self,l,r):
        res=[]
        if l==r:
            return []
        for i in range(l,r):
            
            for j in self.solve(l,i) or [None]:
                for k in self.solve(i+1,r) or [None]:
                    root=TreeNode(i)
                    root.left=j
                    root.right=k
                    res.append(root)
        return res          

sol=Solution()
print(sol.generateTrees(4))
#Runtime: 64 ms, faster than 41.64% of Python3 online submissions for Unique Binary Search Trees II.
#Memory Usage: 15.8 MB, less than 6.67% of Python3 online submissions for Unique Binary Search Trees II.