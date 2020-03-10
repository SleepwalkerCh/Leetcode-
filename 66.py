# 66. Plus One
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i=len(digits)-1
        digits[-1]+=1
        while i>=0:
            if digits[i]==10:
                
                digits[i]=0
                i-=1
                if i!=-1:
                    digits[i]+=1
                else:
                    digits.insert(0,1)
            else:
                break
        return digits
#Runtime: 40 ms, faster than 26.81% of Python3 online submissions for Plus One.
#Memory Usage: 13.7 MB, less than 5.40% of Python3 online submissions for Plus One.