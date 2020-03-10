#105. Construct Binary Tree from Preorder and Inorder Traversal
#递归方法造树，直接通过节点个数将105_1的代码精简了很多
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        now=TreeNode(preorder[0])
        for i in range(len(inorder)):
            if inorder[i]==preorder[0]:
                break
        in_left,in_right=inorder[:i],inorder[i+1:]
        pre_left,pre_right=preorder[1:i+1],preorder[i+1:]
        now.left=self.buildTree(pre_left,in_left)
        now.right=self.buildTree(pre_right,in_right)
        return now
#Runtime: 400 ms, faster than 11.62% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
#Memory Usage: 88.8 MB, less than 7.89% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.        