#97. Interleaving String
# Time Limited 单纯深搜
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if s3=="" and s2=="" and s1=="":
            return True
        if s2=="" or s1=="":
            if s1+s2==s3:
                return True
            else:
                return False
        if s1[0]==s3[0] or s2[0]==s3[0]:
            if s1[0]==s3[0] and s2[0]==s3[0]:
                return (self.isInterleave(s1[1:],s2,s3[1:]) or self.isInterleave(s1,s2[1:],s3[1:]))
            if s1[0]==s3[0]:
                return self.isInterleave(s1[1:],s2,s3[1:])
            if s2[0]==s3[0]:
                return self.isInterleave(s1,s2[1:],s3[1:])
            
        else:
            return False