# 117. Populating Next Right Pointers in Each Node II
#使用116_2的思路，
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
        column=root
        
        while column!=None:
            lastone=None
            row=column
            flag,flagNextLine=True,None
            while row!=None:
                if row.left!=None or row.right!=None:   
                    if row.left!=None and row.right!=None:
                        row.left.next=row.right
                        now=row.left
                    else:
                        now=row.left if row.left!=None else row.right
                    if flag:
                        flagNextLine=now
                        flag=False
                    if lastone!=None:
                        lastone.next=now
                    lastone=row.right if row.right!=None else row.left
                    
                row=row.next
            column=flagNextLine
        return root
#Runtime: 52 ms, faster than 39.45% of Python3 online submissions for Populating Next Right Pointers in Each Node II.
#Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Populating Next Right Pointers in Each Node II.