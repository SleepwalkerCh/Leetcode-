#115. Distinct Subsequences
#超时了
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        num=0
        self.num=num
        self.Do(s,t)
        return self.num
    def Do(self,s:str,t:str):
            if t=="" or s =="" or len(t)>len(s):
                if t=="":
                    self.num+=1
                return
           
            for j in range(len(s)):
                if s[j]==t[0]:
                    self.Do(s[j+1:],t[1:])
            return