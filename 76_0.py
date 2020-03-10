#76. Minimum Window Substring
# 速度很慢，果然超时了，写的很不简洁
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        letters={}
        for letter in t:
            try:
                letters[letter]+=1
            except:
                letters[letter]=1
        
        letterstemp=letters.copy()
        num=0
        summin=len(s)+1
        flag=True
        i,j=0,0
        second=0
        index=[]
        flag=True
        while i<len(s):
            try:
                if letters[s[i]]>0:
                    if num==1 and flag:
                        second=i
                        flag=False
                    if num==0:
                        j=i
                    letters[s[i]]-=1
                    num+=1
                    
                    if num==len(t):
                        if summin>i-j+1:
                            summin=i-j+1
                            index=[i,j]
                        i=max(second,j+1)
                        num=0
                        flag=True
                        letters=letterstemp.copy()
                    else:
                        i+=1
                else:
                    if num==1 and flag:
                        
                        second=i
                        flag=False
                    i+=1
            except:
                i+=1
        if index:
            return s[index[1]:index[0]+1]
        else:
            return ""