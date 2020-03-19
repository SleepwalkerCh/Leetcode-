# 166. Fraction to Recurring Decimal
# 不断 乘10 取模 整除得到循环节
# 有很多边界条件需注意
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        pos=0
        if numerator==0:
            return "0"
        if numerator < 0:
            pos-=1
            numerator=-numerator
        if denominator < 0:
            pos-=1
            denominator=-denominator
        pos=1 if pos%2==0 else -1
        # 处理符号
        IntPart=numerator/denominator
        if pos==-1:
            IntPartStr="-"+str(int(IntPart))
        else:
            IntPartStr=str(int(IntPart))
        if numerator%denominator==0:
            return IntPartStr
        fra=[]
        decstr=""
        numerator=numerator%denominator
        while (not numerator in fra) and numerator!=0:
            fra.append(numerator)
            numerator*=10
            
            decstr=decstr+str(int(numerator/denominator))
            numerator%=denominator
        if numerator!=0:
            for i in range(len(fra)):
                if fra[i]==numerator:
                    break
            decstr=decstr[:i]+"("+decstr[i:]+")"
        
        return IntPartStr+"."+decstr

#Runtime: 40 ms, faster than 9.47% of Python3 online submissions for Fraction to Recurring Decimal.
#Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Fraction to Recurring Decimal.