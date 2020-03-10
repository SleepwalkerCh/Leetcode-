#90. Subsets II
# 与78题思路差的挺多，这种方法不必使用全排列
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        def Insert(nums,l):
            res.append(l[:])
            if nums:
                for i in range(len(nums)):
                    if i>0 and nums[i]==nums[i-1]:
                        continue
                    l.append(nums[i])
                    Insert(nums[i+1:],l)
                    l.pop(-1)
        Insert(nums,[])
        return res
#Runtime: 44 ms, faster than 73.09% of Python3 online submissions for Subsets II.
#Memory Usage: 14.1 MB, less than 5.23% of Python3 online submissions for Subsets II.