#106. Construct Binary Tree from Inorder and Postorder Traversal
#与105_2思路和构造方法基本相同
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        if not postorder:
            return None
        now=TreeNode(postorder[-1])
        for i in range(len(inorder)):
            if inorder[i]==postorder[-1]:
                break
        in_left,in_right=inorder[:i],inorder[i+1:]
        post_left,post_right=postorder[:i],postorder[i:-1]
        now.left=self.buildTree(in_left,post_left)
        now.right=self.buildTree(in_right,post_right)
        return now
#Runtime: 420 ms, faster than 8.21% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
#Memory Usage: 88.9 MB, less than 11.11% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.