#44. Wildcard Matching
#极端数据会超时??
#version 2 将多个*合并超时
#version 3 判定*后单字符匹配,超时
#version 4 判定*后多字符匹配,超时
class Solution:    

    def isMatch(self, s: str, p: str) -> bool:
        i=1
        
        while i<len(p):
            if p[i]=='*' and p[i-1]=='*':
                p=p[:i-1]+p[i:]
            else:
                i+=1
        def check(s,p,num1,num2):
            i=num1
            j=num2
            while j<len(p):
                if i>len(s)-1:
                    if p[j]=='*':
                        return True
                    else:
                        return False
                if p[j] in [s[i],'?']:
                    i+=1
                    j+=1
                elif p[j]=='*':
                    return True
                else:
                    return False
            if (j==len(p)) and (i==len(s)):
                return True
            else:
                return False
        def match(s,p):

            i,j=0,0
            global Index

            while  j<len(p):
                if p[j]!='*':
                    if i>=len(s):
                        return False
                    if p[j] in [s[i],'?']:
                        i+=1
                        j+=1
                    else:
                        return False
                else:
                    if j==len(p)-1:
                        return True
                    else:
                        for k in range(i,len(s)):
                            
                            if check(s,p,k,j+1):
                                Index+=1
                                if match(s[k:],p[j+1:]):
                                    return True
                    return False
            if i==len(s) and j==len(p):
                return True
            else:
                return False
        
        return match(s,p),Index
Index=0
sol=Solution()

print(sol.isMatch("babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb","b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a"))