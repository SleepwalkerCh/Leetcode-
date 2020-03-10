#89. Gray Code
# 简单
class Solution:
    def grayCode(self, n: int) -> List[int]:
        def listTonum(l):
            num=0
            for i in range(len(l)):
                num=num<<1+l[i]
            return num
        code=[]
        for i in range(n):
            code.append(0)
        res=[]
        for i in range(1<<n):
            res.append(listTonum(code))
            if i%2==0:
                code[-1]=1-code[-1]
            else:
                j=n-1
                while j>=0:
                    if code[j]==1:
                        break
                    j-=1
                j-=1
                code[j]=1-code[j]
        return res
            
#Runtime: 44 ms, faster than 21.72% of Python3 online submissions for Gray Code.
#Memory Usage: 14.1 MB, less than 6.45% of Python3 online submissions for Gray Code.