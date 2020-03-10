#116. Populating Next Right Pointers in Each Node
# 借用上种思路继续做
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
            if row.left==None:
                break
            while row!=None:
                
                if lastone!=None:
                    lastone.next=row.left
                row.left.next=row.right
                lastone=row.right
                row=row.next
            column=column.left
        return root
#Runtime: 60 ms, faster than 85.42% of Python3 online submissions for Populating Next Right Pointers in Each Node.
#Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Populating Next Right Pointers in Each Node.