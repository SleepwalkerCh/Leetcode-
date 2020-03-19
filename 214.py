#214. Shortest Palindrome
# 两侧都能加，不符合题意
# 原题查看214_2
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        self.s=s
        if len(s)<2:
            return s
        left,right=(len(s)-1)/2,(len(s)-1)/2
        while left>=0:
            if self.check(round(left-0.6),round(left+0.6)):
                return self.make(left)
            if self.check(round(right-0.6),round(right+0.6)):
                return self.make(right)
            left-=0.5
            right+=0.5
    def check(self,a,b):
        if a<0:
            return True
        while a in range(len(self.s)) and b in range(len(self.s)):
            if self.s[a]!=self.s[b]:
                return False
            a-=1
            b+=1
        return True
    def make(self,axis):
        if axis==(len(self.s)-1)/2:
            return self.s
        elif axis<(len(self.s)-1)/2:
            return self.s[:int(axis*2):-1]+self.s
        else:
            return self.s+self.s[int(axis)*2-len(self.s)]