#108.Convert Sorted Array to Binary Search Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        root=TreeNode(nums[len(nums)//2])
        root.left=self.sortedArrayToBST(nums[:len(nums)//2])
        root.right=self.sortedArrayToBST(nums[len(nums)//2+1:])
        return root
#Runtime: 80 ms, faster than 55.28% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
#Memory Usage: 16.2 MB, less than 6.45% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.