# 21.Merge Two Sorted Lists
#简单的链表合并

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        begin=True
        while l1 and l2:
            if l1.val<l2.val:
                if begin:
                    head=ListNode(l1.val)
                    now=head
                    l1=l1.next
                    begin=False
                else:
                    new=ListNode(l1.val)
                    now.next=new
                    now=new
                    l1=l1.next
            else:
                if begin:
                    head=ListNode(l2.val)
                    now=head
                    l2=l2.next
                    begin=False
                else:
                    new=ListNode(l2.val)
                    now.next=new
                    now=new
                    l2=l2.next
        if l1.next:
            now.next=l2
        else:
            now.next=l1   
        return head
#Runtime: 40 ms, faster than 88.82% of Python3 online submissions for Merge Two Sorted Lists.
#Memory Usage: 13.1 MB, less than 83.99% of Python3 online submissions for Merge Two Sorted Lists.