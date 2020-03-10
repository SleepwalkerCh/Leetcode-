# 171. Excel Sheet Column Number
class Solution:
    def titleToNumber(self, s: str) -> int:
        num=0
        for i in range(len(s)):
            num*=26
            num+=ord(s[i])-ord('A')+1
        return num
#Runtime: 24 ms, faster than 94.04% of Python3 online submissions for Excel Sheet Column Number.
#Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Excel Sheet Column Number.