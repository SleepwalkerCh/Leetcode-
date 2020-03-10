#139. Word Break
#动态规划思路
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        flag=[]
        length=[]
        if len(s)==0:
            return True
        flag.append(True)
        for i in s:
            flag.append(False)
        for i in wordDict:
            if not (len(i) in length):
                length.append(len(i))
        t=0
        while t<len(s):
            if flag[t]:
                for i in length:
                    if t+i>len(s):
                        continue
                    if not flag[t+i]:
                        if s[t:t+i] in wordDict:
                            flag[t+i]=True
            t+=1
        return flag[len(s)]
#Runtime: 36 ms, faster than 70.88% of Python3 online submissions for Word Break.
#Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Word Break.    
