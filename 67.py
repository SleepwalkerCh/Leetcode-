#67. Add Binary
#和66题很像
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        length=max(len(a),len(b))
        while (len(a)<length):
            a="0"+a
        while (len(b)<length):
            b="0"+b
        i=length-1
        t=0
        c=""
        while i>=0:
            num=int(a[i])+int(b[i])+t
            if num>=2:
                num-=2
                t=1
            else:
                t=0
            c=str(num)+c
            i-=1
        if t==1:
            c="1"+c
        return c
#Runtime: 60 ms, faster than 5.00% of Python3 online submissions for Add Binary.
#Memory Usage: 13.8 MB, less than 5.09% of Python3 online submissions for Add Binary.