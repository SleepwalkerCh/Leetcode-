#82. Remove Duplicates from Sorted List II
#略显冗长
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        begin=ListNode(0)
        begin.next=head
        forward=begin
        flag=False
        if not head:
            return head
        while head.next:
            if head.val==head.next.val:
                head.next=head.next.next
                flag=True
            else:
                if flag:
                    forward.next=head.next
                    head=head.next
                    flag=False
                else:
                    forward=head
                    head=head.next
        if flag:
            forward.next=head.next
            head=head.next
            flag=False
        return begin.next
#Runtime: 48 ms, faster than 70.51% of Python3 online submissions for Remove Duplicates from Sorted List II.
#Memory Usage: 13.9 MB, less than 5.43% of Python3 online submissions for Remove Duplicates from Sorted List II.