#116. Populating Next Right Pointers in Each Node
# 非固定额外空间需求，废弃
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        old=[]
        if root:
            old.append(root)
        else:
            return root
        print(old)
        while old[0]!=None:
            new=[]
            for i in range(len(old)-1):
                old[i].next=old[i+1]
            for i in old:
                if i.left:
                    new.append(i.left)
                    new.append(i.right)
            old[:]=new[:]
        return root
