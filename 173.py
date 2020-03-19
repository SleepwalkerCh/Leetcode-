# 173. Binary Search Tree Iterator
# 栈存储
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root=root
        self.stack=[]
        while root!=None:
            self.stack.append(root)
            root=root.left
        
    def next(self) -> int:
        """
        @return the next smallest number
        """
    
        if self.stack==[]:
            return
        
        num=self.stack[-1].val
        now=self.stack.pop()
        if now.right!=None:
            now=now.right
            while now!=None:
                self.stack.append(now)
                now=now.left
        return num
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.stack!=[]:
            return True
        else:
            return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

#Runtime: 80 ms, faster than 49.29% of Python3 online submissions for Binary Search Tree Iterator.
#Memory Usage: 20.1 MB, less than 15.38% of Python3 online submissions for Binary Search Tree Iterator.