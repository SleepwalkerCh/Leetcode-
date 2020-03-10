#97. Interleaving String
# 深搜且存储
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        self.flag=[]
        for i in range(len(s1)):
            self.flag.append([])
            for j in s2:
                self.flag[i].append(-1)
        self.s1,self.s2,self.s3=s1,s2,s3
        if self.Do(0,0,0) > 0:
            return True 
        else:
            return False
    def Do(self,i,j,t):
        if i==len(self.s1) or j==len(self.s2):
            if self.s1[i:]+self.s2[j:]==self.s3[t:]:
               
                return 1
            else:
                 
                return 0
        elif t==len(self.s3):
            self.flag[i][j]=0
            return self.flag[i][j]
        if self.flag[i][j]>-1:
            return self.flag[i][j]
        if self.s1[i]==self.s3[t] or self.s2[j]==self.s3[t]:
            if self.s1[i]==self.s3[t] and self.s2[j]==self.s3[t]:
                self.flag[i][j]=1 if self.Do(i+1,j,t+1) + self.Do(i,j+1,t+1) > 0 else 0
            elif self.s1[i]==self.s3[t]:
                self.flag[i][j]= self.Do(i+1,j,t+1)
            elif self.s2[j]==self.s3[t]:
                self.flag[i][j]= self.Do(i,j+1,t+1)
            return self.flag[i][j]
        else:
            self.flag[i][j]=0
            return 0
#Runtime: 32 ms, faster than 76.01% of Python3 online submissions for Interleaving String.
#Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Interleaving String.