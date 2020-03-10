#101. Symmetric Tree
#栈结构存储，dfs，非递归
#用一个栈也能解决问题
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        l_stack,r_stack=[],[]
        if not root:
            return True
        
        l=root.left
        r=root.right
        if l==r==None:
            return True

        while True:
            if l==None or r==None:
                if l==None and r==None:
                    if not l_stack or not r_stack:
                        if not l_stack and not r_stack:
                            return True
                        else:
                            return False
                    l=l_stack.pop().right
                    r=r_stack.pop().left
                    continue
                else:
                    return False
            
            if l.val!=r.val:
                return False
            l_stack.append(l)
            r_stack.append(r)
            l_status=r_status=0

            l=l.left
            r=r.right
#Runtime: 44 ms, faster than 41.02% of Python3 online submissions for Symmetric Tree.
#Memory Usage: 14.1 MB, less than 5.17% of Python3 online submissions for Symmetric Tree.
           