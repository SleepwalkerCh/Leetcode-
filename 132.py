# 132. Palindrome Partitioning II
# 算上记录的dfs
class Solution:
    def minCut(self, s: str) -> int:
        
        self.res=[]
        
        self.su=[-1]*(len(s)+1)
        self.su[0]=1
        return self.helper(s)
        
    def helper(self,s):
        minnum=len(s)    
        if s=="":
            return 0
        for i in range(len(s)):
            if s[:i+1]==s[i::-1]:  
                if self.su[len(s)-i-1]==-1:
                    self.su[len(s)-i-1]=self.helper(s[i+1:])
                if minnum>=self.su[len(s)-i-1]:
                    minnum=self.su[len(s)-i-1]
        self.su[len(s)]=minnum
        return minnum
#Runtime: 952 ms, faster than 15.14% of Python3 online submissions for Palindrome Partitioning II.
#Memory Usage: 14.9 MB, less than 90.00% of Python3 online submissions for Palindrome Partitioning II.