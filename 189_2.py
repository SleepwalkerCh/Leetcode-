#189. Rotate Array
# 直接拼凑list 空间使用量过大
# 

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        temp=nums[-k:]
        nums[:]=temp[:]+nums[:-k]
        return 
#Runtime: 60 ms, faster than 80.72% of Python3 online submissions for Rotate Array.
#Memory Usage: 14.1 MB, less than 5.09% of Python3 online submissions for Rotate Array.