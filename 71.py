#71. Simplify Path
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        stack=path.split("/")
        i=0
        while i<len(stack):
            if stack[i]=="" or stack[i]==".":
                del(stack[i])
            else:
                i+=1
        i=len(stack)-1
        delete=0
        res=""
        while i>=0:
            if stack[i]=="..":
                delete+=1
            elif delete==0:
                res="/"+stack[i]+res
            else:
                delete-=1
            i-=1
        return res
#Runtime: 40 ms, faster than 61.19% of Python3 online submissions for Simplify Path.
#Memory Usage: 13.7 MB, less than 5.49% of Python3 online submissions for Simplify Path.