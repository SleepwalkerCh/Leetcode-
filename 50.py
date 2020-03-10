#50. Pow(x, n)
#简单的递归就可以了
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x=1/x
            n=-1*n
        if n==0:
            return 1
        else:
            if n%2==1:
                return (self.myPow(x,n//2)**2)*x
            else:
                return self.myPow(x,n//2)**2
#Runtime: 32 ms, faster than 88.75% of Python3 online submissions for Pow(x, n).
#Memory Usage: 13.2 MB, less than 58.35% of Python3 online submissions for Pow(x, n).