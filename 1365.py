#1365. How Many Numbers Are Smaller Than the Current Number
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        barrel=[]
        for i in range(102):
            barrel.append(0)
        for i in nums:
            barrel[i+1]+=1
        for i in range(len(barrel)-1):
            barrel[i+1]+=barrel[i]
        res=[]
        for i in nums:
            res.append(barrel[i])
        return res
#Runtime: 52 ms, faster than 86.13% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
#Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.