#96. Unique Binary Search Trees
#直接求95list的长度会超时 非递归方法 直接数组存之前结果
# 结果比直接递归快了很多
class Solution:
    def numTrees(self, n: int) -> int:
        res=[]
        for i in range(n+1):
            if i<=1:
                res.append(1)
            else:
                res.append(0)
        for i in range(2,n+1):
            for j in range(i):
                res[i]+=res[i-1-j]*res[j]
        return res[n]
#Runtime: 36 ms, faster than 66.71% of Python3 online submissions for Unique Binary Search Trees.
#Memory Usage: 13.9 MB, less than 10.71% of Python3 online submissions for Unique Binary Search Trees.