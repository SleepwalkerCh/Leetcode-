#43. Multiply Strings
#高精度做法
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def isZero(num: str):
            if len(num)==1:
                if num[0]=='0':
                    return True
            return False
        def product(n1,n2,step):
            plus=0
            res=""
            for i in range(len(n2)):
                now=int(n2[len(n2)-i-1])
                nowres=str(plus+n1*now)
                if len(nowres)==1:
                    plus=0
                else:
                    plus=int(nowres[0])
                res=nowres[-1]+res
            if plus>0:
                res=str(plus)+res
            for i in range(step):
                res+="0"
            return res
        def Plus(s1,s2):
            if not s1:
                return s2
            if not s2:
                return s1
            if len(s1)>len(s2):
                for i in range(len(s1)-len(s2)):
                    s2="0"+s2
                length=len(s1)
            else:
                for i in range(len(s2)-len(s1)):
                    s1="0"+s1
                length=len(s2)
            plus=0
            res=""
            for i in range(length):
                now=int(s1[-i-1])+int(s2[-i-1])+plus
                if now>=10:
                    plus=1
                else:
                    plus=0
                res=str(now)[-1]+res

            if plus>0:
                return "1"+res
        
            return res

        if isZero(num1) or isZero(num2):
            return "0"
        result=""
        for i in range(len(num1)):
            if not isZero(str(num1[len(num1)-1-i])):
                pro=product(int(num1[len(num1)-1-i]),num2,i)
            else:
                pro=""
            result=Plus(pro,result)
        return result
sol=Solution()
print(sol.multiply("123","456"))
#Runtime: 364 ms, faster than 5.15% of Python3 online submissions for Multiply Strings.
#Memory Usage: 13.3 MB, less than 29.95% of Python3 online submissions for Multiply Strings.
