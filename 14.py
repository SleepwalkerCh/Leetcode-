#14. Longest Common Prefix  
#简单的查找比对，没啥意义的一道题
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=""
        i=0
        length=255
        if len(strs)==0:
            return prefix
        for st in strs:
            if len(st)<=length:
                length=len(st)
        
        for i in range(length):
            letter=strs[0][i]
            for st in strs:
                if st[i]!=letter:
                    return prefix
            prefix+=letter
        return prefix