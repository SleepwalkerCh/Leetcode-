# Definition for a binary tree node.
# 自己花了很久都没琢磨明白的方法，至今没有成功
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import copy
class Solution:
    def generateTrees(self, n: int):
        res=[]
        self.res=res
        self.n=n

        root=TreeNode(0)
        
        self.deal(1,n,root,root,1)
        return self.res

    def deal(self,n1,n2,root,realroot,mark):
        if n1==n2: 
            root.val=n1
            if mark==self.n:
                self.res.append(copy.deepcopy( realroot ))
             
        else:
            for i in range(n1,n2+1):
                root.val=i
                root.left=None
                root.right=None
                flag=0
                if n1!=i:
                    mark+=1
                    flag+=1
                    root.left=TreeNode(0)
                    self.deal(n1,i-1,root.left,realroot,mark)
                if i!=n2:
                    mark+=1
                    flag+=1
                    root.right=TreeNode(0)
                    self.deal(i+1,n2,root.right,realroot,mark)
                mark-=flag
                  
sol=Solution()
print(sol.generateTrees(4))
#        3
#     1     4 
#      2      
#[[1,null,2,null,3,null,4,null,5],[1,null,2,null,3,null,5,4],[1,null,2,null,4,3,5],[1,null,2,null,5,3,null,null,4],[1,null,2,null,5,4,null,3],[1,null,3,2,4,null,null,null,5],[1,null,3,2,5,null,null,4],[1,null,5,2,null,null,3,null,4],[1,null,5,2,null,null,4,3],[1,null,5,3,null,2,4],[1,null,5,4,null,2,null,null,3],[1,null,5,4,null,3,null,2],[2,1,3,null,null,null,4,null,5],[2,1,3,null,null,null,5,4],[2,1,4,null,null,3,5],[2,1,5,null,null,3,null,null,4],[2,1,5,null,null,4,null,3],[5,1,null,null,2,null,3,null,4],[5,1,null,null,2,null,4,3],[5,1,null,null,3,2,4],[5,1,null,null,4,2,null,null,3],[5,1,null,null,4,3,null,2],[5,2,null,1,3,null,null,null,4],[5,2,null,1,4,null,null,3],[5,4,null,1,null,null,2,null,3],[5,4,null,1,null,null,3,2],[5,4,null,2,null,1,3],[5,4,null,3,null,1,null,null,2],[5,4,null,3,null,2,null,1]]
[[1,null,2,null,3,null,4,null,5],[1,null,2,null,3,null,5,4],[1,null,2,null,4,3,5],[1,null,2,null,5,3,null,null,4],[1,null,2,null,5,4,null,3],[1,null,3,2,4,null,null,null,5],[1,null,3,2,5,null,null,4],[1,null,5,2,null,null,3,null,4],[1,null,5,2,null,null,4,3],[1,null,5,3,null,2,4],[1,null,5,4,null,2,null,null,3],[1,null,5,4,null,3,null,2],[2,1,3,null,null,null,4,null,5],[2,1,3,null,null,null,5,4],[2,1,4,null,null,3,5],[2,1,5,null,null,3,null,null,4],[2,1,5,null,null,4,null,3],[5,1,null,null,2,null,3,null,4],[5,1,null,null,2,null,4,3],[5,1,null,null,3,2,4],[5,1,null,null,4,2,null,null,3],[5,1,null,null,4,3,null,2],[5,2,null,1,3,null,null,null,4],[5,2,null,1,4,null,null,3],[5,4,null,1,null,null,2,null,3],[5,4,null,1,null,null,3,2],[5,4,null,2,null,1,3],[5,4,null,3,null,1,null,null,2],[5,4,null,3,null,2,null,1]]
#[[1,null,2,null,3,null,4,null,5],[1,null,2,null,3,null,5,4],[1,null,2,null,4,3,5],[1,null,2,null,5,3,null,null,4],[1,null,2,null,5,4,null,3],[1,null,3,2,4,null,null,null,5],[1,null,3,2,5,null,null,4],[1,null,4,2,5,null,3],[1,null,4,3,5,2],[1,null,5,2,null,null,3,null,4],[1,null,5,2,null,null,4,3],[1,null,5,3,null,2,4],[1,null,5,4,null,2,null,null,3],[1,null,5,4,null,3,null,2],[2,1,3,null,null,null,4,null,5],[2,1,3,null,null,null,5,4],[2,1,4,null,null,3,5],[2,1,5,null,null,3,null,null,4],[2,1,5,null,null,4,null,3],[3,1,4,null,2,null,5],[3,1,5,null,2,4],[3,2,4,1,null,null,5],[3,2,5,1,null,4],[4,1,5,null,2,null,null,null,3],[4,1,5,null,3,null,null,2],[4,2,5,1,3],[4,3,5,1,null,null,null,null,2],[4,3,5,2,null,null,null,1],[5,1,null,null,2,null,3,null,4],[5,1,null,null,2,null,4,3],[5,1,null,null,3,2,4],[5,1,null,null,4,2,null,null,3],[5,1,null,null,4,3,null,2],[5,2,null,1,3,null,null,null,4],[5,2,null,1,4,null,null,3],[5,3,null,1,4,null,2],[5,3,null,2,4,1],[5,4,null,1,null,null,2,null,3],[5,4,null,1,null,null,3,2],[5,4,null,2,null,1,3],[5,4,null,3,null,1,null,null,2],[5,4,null,3,null,2,null,1]]
            

#[[1,null,2,null,3,null,4],[1,null,2,null,4,3],[1,null,3,2,4],[1,null,4,2,null,null,3],[1,null,4,3,null,2],[2,1,3,null,null,null,4],[2,1,4,null,null,3],[4,1,null,null,2,null,3],[4,1,null,null,3,2],[4,2,null,1,3],[4,3,null,1,null,null,2],[4,3,null,2,null,1]]
#[[1,null,2,null,3,null,4],[1,null,2,null,4,3],[1,null,3,2,4],[1,null,4,2,null,null,3],[1,null,4,3,null,2],[2,1,3,null,null,null,4],[2,1,4,null,null,3],[3,1,4,null,2],[3,2,4,1],[4,1,null,null,2,null,3],[4,1,null,null,3,2],[4,2,null,1,3],[4,3,null,1,null,null,2],[4,3,null,2,null,1]]