#10. Regular Expression Matching
#每次到*就递归一次，
# 关键语句
# return  isMatch(s,p[2:]) or isMatch(s[1:],p)
def isMatch(s: str, p: str) -> bool:
    if (not p):
        if (not s):
            return True
        else:
            return False
    flag=False
    if (s):
        if (s[0]==p[0]) or (p[0]=="."):
            flag=True
    if len(p)>1:
        if p[1]=="*":
            if flag:
                return  isMatch(s,p[2:]) or isMatch(s[1:],p)
            else:
                return isMatch(s,p[2:])
        else:
            if flag:
                return isMatch(s[1:],p[1:])
            else:
                return False
    else:
        if flag:
            return isMatch(s[1:],p[1:])
        else:
            return False
