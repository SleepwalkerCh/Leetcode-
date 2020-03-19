# 202. Happy Number
class Solution:
    def isHappy(self, n: int) -> bool:
        numlist=[]
        while (not n in numlist) and n!=1:
            print(n)
            if n<1000:
                numlist.append(n)
            n=self.helper(n)
        if n==1:
            return True
        else:
            return False
    def helper(self,n):
        sumnum=0
        while n!=0:
            sumnum+=(n%10)*(n%10)
            n=n//10
        return sumnum
#Runtime: 32 ms, faster than 67.35% of Python3 online submissions for Happy Number.
#Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Happy Number.