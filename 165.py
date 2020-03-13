#165. Compare Version Numbers
# 简单切割对比
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1,v2=version1.split("."),version2.split(".")
        v1int,v2int=[int(i) for i in v1],[int(i) for i in v2]
        i=0
        while i<len(v1int) and i<len(v2int):
            if v1int[i]>v2int[i]:
                return 1
            if v1int[i]<v2int[i]:
                return -1
            i+=1
        if len(v1int)==len(v2int):
            return 0
        if len(v1int)<len(v2int):
            for j in range(i,len(v2int)):
                if v2int[j]!=0:
                    return -1
            return 0
        if len(v1int)>len(v2int):
            for j in range(i,len(v1int)):
                if v1int[j]!=0:
                    return 1
            return 0
#Runtime: 20 ms, faster than 96.64% of Python3 online submissions for Compare Version Numbers.
#Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Compare Version Numbers.