#28. Implement strStr()
# 这道题可以先从暴力匹配开始做起 (1) 暴力匹配看起来效果也还可以

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i=j=0
        while j<len(needle) or len(haystack)-len(needle)+1>i:
            if haystack[i]==needle[j]:
                i+=1
                j+=1
            else:
                i=i-j+1
                j=0
        if j==len(needle):
            return i-j
        else:
            return -1
#Runtime: 44 ms, faster than 35.66% of Python3 online submissions for Implement strStr().
#Memory Usage: 13.2 MB, less than 80.02% of Python3 online submissions for Implement strStr().