#28. Implement strStr()
#使用KMP算法对速度进行了小部分优化
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        next=[-1]
        k=-1
        j=0
        while j<len(needle):
            if k==-1 or needle[j]==needle[k]:
                k+=1
                j+=1
                next.append(k)
            else:
                k=next[k]

        i=0
        j=0
        while i<len(haystack) or (j==len(needle)):
            if j==len(needle):
                return i-j
            if j!=-1 and haystack[i]!=needle[j]:
                j=next[j]
            else:
                j+=1
                i+=1
        return -1
#Runtime: 52 ms, faster than 21.21% of Python3 online submissions for Implement strStr().
#Memory Usage: 14.5 MB, less than 5.01% of Python3 online submissions for Implement strStr().
# 使用Python提供的API会使运行速度变得很快，代码量也会变得非常精炼，但是它毫无意义
        