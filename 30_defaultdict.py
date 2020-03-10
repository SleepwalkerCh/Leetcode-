#30. Substring with Concatenation of All Words
# 代码存在冗余部分。使用的是借助字典的简单遍历
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words)==0:
            return []
        length=len(words[0])
        word={}
        num=len(words)
        for i in words:
            try:
                word[i]+=1
            except:
                word[i]=1
        wordtemp=word.copy()
        i=0    
        flag=True
        res=[]
        while i+length<=len(s):# i+num*length<=len(s) 更省时间
            try:
                if word[s[i:i+length]]>0:
                    
                    word[s[i:i+length]]-=1
                    num-=1
                    if flag:
                        flag=False
                        start=i
                    if num==0:
                        res.append(start)
                        flag=True
                        num=len(words)
                        word=wordtemp.copy()
                        i=start+1
                    else:
                        i+=length
                else:
                    if not flag:
                        flag=True
                        num=len(words)
                        word=wordtemp.copy()
                    i=1+start
            except:
                if not flag:
                    flag=True
                    num=len(words)
                    word=wordtemp.copy()
                    i=start+1 
                else:
                    i+=1
        return res

#Runtime: 580 ms, faster than 37.82% of Python3 online submissions for Substring with Concatenation of All Words.
#Memory Usage: 13.9 MB, less than 6.50% of Python3 online submissions for Substring with Concatenation of All Words.

#from collections import Counter, defaultdict
#seen = defaultdict(int)