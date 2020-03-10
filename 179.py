#179. Largest Number
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        numstr=[]
        for i in nums:
            numstr.append(str(i))
        numstr.sort(reverse=True)
        res=""
        for i in numstr:
            res+=i
        return res