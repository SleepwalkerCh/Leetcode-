#131. Palindrome Partitioning
# 粗暴 dfs
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res=[]
        self.helper(s,[])
        return self.res
    def helper(self,s,l):
        if s=="":
            self.res.append(l[:])
        for i in range(len(s)):
            if s[:i+1]==s[i::-1]:
                print(s[:i+1])
                l.append(s[:i+1])
                self.helper(s[i+1:],l)
                l.pop()
#Runtime: 64 ms, faster than 90.17% of Python3 online submissions for Palindrome Partitioning.
#Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Palindrome Partitioning.