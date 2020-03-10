#88. Merge Sorted Array
#
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j,num=0,0,0
        while num<m and j<n:
            if nums1[i]<=nums2[j]:
                i+=1
                num+=1
            else:
                nums1.insert(i,nums2[j])
                j+=1
                i+=1
                nums1.pop(-1)
        if num==m:
            while j<n:
                nums1.insert(i,nums2[j])
                j+=1
                i+=1
                nums1.pop(-1)

#Runtime: 56 ms, faster than 13.61% of Python3 online submissions for Merge Sorted Array.
#Memory Usage: 14 MB, less than 5.08% of Python3 online submissions for Merge Sorted Array.