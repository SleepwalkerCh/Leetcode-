# 203. Remove Linked List Elements
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        mark=ListNode(0)
        mark.next=head
        last=mark
        while head!=None:
            if head.val==val:
                last.next=head.next
            else:
                last=head
            head=head.next
        return mark.next
#Runtime: 72 ms, faster than 46.46% of Python3 online submissions for Remove Linked List Elements.
#Memory Usage: 16 MB, less than 100.00% of Python3 online submissions for Remove Linked List Elements.