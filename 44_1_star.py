#44. Wildcard Matching
# 根据44_他人代码.py 他人的思路完成代码 很强
class Solution:    
    def isMatch(self, s: str, p: str) -> bool:
        i,j=0,0
        def match(s,p,status):
            i,j=0,0
            mark=0
            while i<len(s):
                if j>len(p)-1:
                    if status:
                        j=0
                        mark+=1
                        i=mark
                    else:
                        return False
                else:
                    if p[j] in [s[i],'?']:
                        i+=1
                        j+=1
                    elif p[j]=='*':
                        return match(s[i:],p[j+1:],1)
                    elif status:
                        j=0
                        mark+=1
                        i=mark
                    else:
                        return False
            while j<len(p):
                if p[j]=='*':
                    j+=1
                else:
                    return False
            return True
        return match(s,p,0)
#Runtime: 56 ms, faster than 95.50% of Python3 online submissions for Wildcard Matching.
#Memory Usage: 13.4 MB, less than 64.36% of Python3 online submissions for Wildcard Matching.