#69. Sqrt(x)
#二分法找

class Solution:
    def mySqrt(self, x: int) -> int:
        if x<=1:
            return x
        a,b=1,x-1
        while a!=b:
            if ((a+b)//2)**2==x:
                return (a+b)//2
            if ((a+b)//2)**2>x:
                b=(a+b)//2
            else:
                a=(a+b)//2+1
        if a**2>x:
            return a-1
        else:
            return a

#Runtime: 56 ms, faster than 20.34% of Python3 online submissions for Sqrt(x).
#Memory Usage: 13.8 MB, less than 5.23% of Python3 online submissions for Sqrt(x).