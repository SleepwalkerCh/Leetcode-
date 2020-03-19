#140. Word Break II
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if s in wordDict:
            return [s]
        self.wordDict=wordDict
        
        self.res=[]
        self.dfs(s,[])
        return [" ".join(i) for i in self.res]
    def dfs(self,s,resstr):
        if s == "":
            self.res.append(resstr)
            return
        for word in self.wordDict:
            if not s.startswith(word):
                continue
            
            self.dfs(s[len(word):],resstr[:]+[word])
            
        return
                