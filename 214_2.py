#214. Shortest Palindrome
# 每一字节check会超时
# 用数组切片直接比对会加快速度
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        self.s=s
        if len(s)<2:
            return s
        left=(len(s)-1)/2
        while left>=0:
            if self.check(round(left-0.6),round(left+0.6)):
                return self.make(left)    
            left-=0.5
    def check(self,a,b):
        #print(a,b,self.s[:a+1],self.s[a+b+1:b-1:-1])
        return self.s[:a+1]==self.s[a+b+1:b-1:-1]
        # while a>=0 and b <len(self.s):
        #     if self.s[a]!=self.s[b]:
        #         return False
        #     a-=1
        #     b+=1
        # return True
    def make(self,axis):
        if axis==(len(self.s)-1)/2:
            return self.s
        else:
            return self.s[:int(axis*2):-1]+self.s
#Runtime: 216 ms, faster than 33.65% of Python3 online submissions for Shortest Palindrome.
#Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Shortest Palindrome.