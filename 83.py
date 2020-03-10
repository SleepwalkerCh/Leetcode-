#83. Remove Duplicates from Sorted List
# 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        forward=head
        begin=head
        try:
            head=head.next
        except:
            return head
        while head:
            if head.val==forward.val:
                forward.next=head.next
            else:
                forward=head
            head=head.next
        return begin
#Runtime: 48 ms, faster than 71.06% of Python3 online submissions for Remove Duplicates from Sorted List.
#Memory Usage: 14 MB, less than 5.58% of Python3 online submissions for Remove Duplicates from Sorted List.