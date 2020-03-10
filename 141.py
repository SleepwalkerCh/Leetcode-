#141. Linked List Cycle
# 快慢指针
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fp,sp=head,head
        while fp.next.next!=nil and sp.next!=nil:
            fp=fp.next.next
            sp=sp.next
            if fp==sp:
                return True
        return False
#Runtime: 48 ms, faster than 64.30% of Python3 online submissions for Linked List Cycle.
#Memory Usage: 16.1 MB, less than 100.00% of Python3 online submissions for Linked List Cycle.