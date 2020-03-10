# 38. Count and Say
# 简单的递归做法
class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        st=self.countAndSay(n-1)
        if len(st)==1:
            return "1"+st
        newst=""
        i,count=1,1
        while i<len(s):
            if st[i]==st[i-1]:
                count+=1
                
            else:
                newst+=str(count)+str(st[i-1])
                count=1
            i+=1
        newst+=str(count)+str(len(s))
        return newst

# Runtime: 44 ms, faster than 35.23% of Python3 online submissions for Count and Say.
# Memory Usage: 13.3 MB, less than 24.43% of Python3 online submissions for Count and Say.