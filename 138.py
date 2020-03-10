# 138. Copy List with Random Pointer
# 三轮遍历
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        a=head
        while a != None:
            newNode=Node(a.val)
            newNode.next=a.next
            a.next=newNode
            a=a.next.next
        a=head
        while a!= None:
            if a.random!=None:
                a.next.random=a.random.next
            else:
                a.next.random=None
            a=a.next.next
        a=head
        newhead=Node(0)
        b=newhead
        while a!= None:
            b.next=a.next
            b=b.next
            a=a.next.next
        return newhead.next
#Runtime: 32 ms, faster than 78.86% of Python3 online submissions for Copy List with Random Pointer.
#Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Copy List with Random Pointer.