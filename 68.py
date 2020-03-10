# 68. Text Justification
# 没啥好说的
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        now,num=[],0
        res=[]
        for word in words:
            if len(now)+len(word)+num>maxWidth:
                for i in range(maxWidth-num-len(now)):
                    now[i%((len(now)-1) or 1)]+=" "
                res.append("")
                for i in range(len(now)):
                    if i==len(now)-1:
                        now[i]+=" "
                    res[-1]+=now[i]
                now,num=[],0
            now.append(word)
            num+=len(word)
        res.append("")
        for i in now:
            res[-1]+=i
        for i in range(maxWidth-len(now)-num):
            res[-1]+=" "
        return res
        
#Runtime: 32 ms, faster than 96.34% of Python3 online submissions for Text Justification.
#Memory Usage: 14 MB, less than 6.75% of Python3 online submissions for Text Justification.