#189. Rotate Array
#一步步移动，直接做会超时 v1.1
#分左移右移做,还是会超时 v1.2

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        temp=nums[-k:]
        return temp+nums
