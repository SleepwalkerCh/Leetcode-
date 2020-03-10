#91. Decode Ways
# 找规律，斐波那契数列和特殊0的处理实现解决
class Solution:
    def numDecodings(self, s: str) -> int:
        numlist=[]
        i,j=0,0
        for i in range(len(s)):
            if s[i] not in ('1','2'):
                
                numlist.append(s[j:i+1])
                j=i+1
        if s[j:i+1]:
            numlist.append(s[j:i+1])
        numsum=1
        def fibo(n):
            if n<=3:
                return n
            else:
                return fibo(n-2)+fibo(n-1)
        for i in numlist:
            if i[-1]=='0' and (len(i)==1 or i[-2] not in ('1','2'))  :
                    res=0
            else:
                if len(i)==1:
                    res=1
                elif len(i)==2:
                    if int(i)<=26 and int(i)%10!=0:
                        res=2
                    else:
                        res=1
                else:
                    if int(i[-2:])>26:
                        res=fibo(len(i)-1)
                    else:
                        if int(i[-2:]) % 10!=0:
                            res=fibo(len(i))
                        else:
                            res=fibo(len(i)-2)
            numsum*=res
        return numsum
#Runtime: 36 ms, faster than 87.00% of Python3 online submissions for Decode Ways.
#Memory Usage: 13.9 MB, less than 16.57% of Python3 online submissions for Decode Ways.
