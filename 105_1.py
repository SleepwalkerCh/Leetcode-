#105. Construct Binary Tree from Preorder and Inorder Traversal
#递归方法造树，速度有点慢而且代码冗长
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if preorder:
            root=TreeNode(preorder[0])
        else:
            return None

        return self.Build(preorder,inorder)
    def Build(self,preorder,inorder):
        #print(preorder,inorder)
        if not preorder:
            return None
        now=TreeNode(preorder[0])
        for i in range(len(inorder)):
            if inorder[i]==preorder[0]:
                break
        #print(i)
        in_left=inorder[:i]
        in_right=inorder[i+1:]
        if in_right:
            for i in range(len(preorder)):
                if preorder[i] in in_right:
                    break
            
            pre_left=preorder[1:i]
            pre_right=preorder[i:]
        else:
            pre_left=preorder[1:]
            pre_right=[]
        #print(pre_left,pre_right,in_left,in_right)
        now.left=self.Build(pre_left,in_left)
        now.right=self.Build(pre_right,in_right)
        return now
#Runtime: 444 ms, faster than 8.74% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
#Memory Usage: 89 MB, less than 5.26% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.