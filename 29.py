#29. Divide Two Integers
#用位运算替代乘法操作
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        flag=True
        if dividend<0:
            flag=not flag
        if divisor<0:
            flag=not flag
        dividend=abs(dividend)
        divisor=abs(divisor)
        result=0
        while dividend>=divisor:
            now=divisor<<0
            nowresult=-1
            while dividend>=now:
                now=now<<1
                nowresult+=1
            if nowresult>=0:
                result+=1<<nowresult
                dividend-=divisor<<nowresult
        if not flag:
            result=result*-1
        if result>(1<<31)-1:
            return (1<<31)-1
        else:
            return result
#Runtime: 32 ms, faster than 95.80% of Python3 online submissions for Divide Two Integers.
#Memory Usage: 13.3 MB, less than 20.02% of Python3 online submissions for Divide Two Integers.
# 10 3 3
# 10 -3 -3
# -10 3 -3
# -10 -3