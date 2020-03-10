#76. Minimum Window Substring
# 该题花了很久，这个思路还需要再细细琢磨

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        i,j=0,0
        letters={}
        for i in range(128):
            letters[i]=0
        for i in t:
            letters[ord(i)]+=1
        i=0
        num=0
        nmin=len(s)+1
        l,r=-1,-1
        while i<len(s):
            
            letters[ord(s[i])]-=1
            if letters[ord(s[i])]>=0:
                if num==0:
                    start=i
                num+=1
            while num==len(t):
                letters[ord(s[start])]+=1
                if nmin>i-start+1:
                    nmin=i-start+1
                    l,r=start,i
                letters[ord(s[start])]+=1
                start+=1
                
                if letters[ord(s[start])]>0:
                    num-=1
                start+=1
            i++
        if l==-1:
            return ""
        return s[l:r+1]
#Runtime: 244 ms, faster than 18.63% of Python3 online submissions for Minimum Window Substring.
#Memory Usage: 14.9 MB, less than 10.78% of Python3 online submissions for Minimum Window Substring.
