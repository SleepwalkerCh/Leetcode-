#115. Distinct Subsequences
# 动态规划做法成功
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        num=[]
        if t=="":
            return 1
        if s=="":
            return 0
        for i in range(len(t)+1):
            num.append([])
            for j in range(len(s)+1):
                if i==len(t):
                    num[i].append(1)
                elif j==len(s):
                    num[i].append(0)
                else:
                    num[i].append(-1)
        self.num=num
        self.s=s
        self.t=t
        print(self.Do(0,0))
        return self.Do(0,0)
    def Do(self,i,j):
        if self.num[i][j]!=-1:
            return self.num[i][j]
        if self.t[i]==self.s[j]:
            self.num[i][j]=self.Do(i+1,j+1)+self.Do(i,j+1)
            return self.num[i][j]
        else:
            self.num[i][j]=self.Do(i,j+1)
            return self.num[i][j]
sol=Solution()
sol.numDistinct("daacaedaceacabbaabdccdaaeaebacddadcaeaacadbceaecddecdeedcebcdacdaebccdeebcbdeaccabcecbeeaadbccbaeccbbdaeadecabbbedceaddcdeabbcdaeadcddedddcececbeeabcbecaeadddeddccbdbcdcbceabcacddbbcedebbcacca","ceadbaa")
#sol.numDistinct("abccddde","cdd")

#Runtime: 340 ms, faster than 11.06% of Python3 online submissions for Distinct Subsequences.
#Memory Usage: 25.9 MB, less than 57.14% of Python3 online submissions for Distinct Subsequences.