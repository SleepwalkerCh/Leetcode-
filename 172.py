# 172. Factorial Trailing Zeroes
class Solution:
    def trailingZeroes(self, n: int) -> int:
        num=0
        while n>0:
            num+=n//5
            n=n//5
        return num
#Runtime: 24 ms, faster than 89.17% of Python3 online submissions for Factorial Trailing Zeroes.
#Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Factorial Trailing Zeroes.