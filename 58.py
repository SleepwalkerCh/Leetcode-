# 58. Length of Last Word
#没啥可说的
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i=len(s)-1
        while i>=0:
            if s[i]!=" ":
                break
            i-=1
        res=0
        while i>=0:
            if s[i]==" ":
                break
            res+=1
            i-=1
        return res
#Runtime: 40 ms, faster than 17.35% of Python3 online submissions for Length of Last Word.
#Memory Usage: 14 MB, less than 5.37% of Python3 online submissions for Length of Last Word.