# 168. Excel Sheet Column Title
class Solution:
    def convertToTitle(self, n: int) -> str:
        res=""
        
        while n>0:
            res=(n+25)%26+'A'+res
            n=n//26
        return res
#Runtime: 28 ms, faster than 58.24% of Python3 online submissions for Excel Sheet Column Title.
#Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Excel Sheet Column Title.