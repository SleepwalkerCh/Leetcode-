#86. Partition List
# 题目不难，但是需要对对象理解更深
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        left=ListNode(0)
        right=ListNode(0)
        firstleft,firstright=left,right
        while head:
            if head.val<x:
                left.next=head
                left=left.next
            else:
                right.next=head
                right=right.next
            head=head.next
        right.next=None
        left.next=firstright.next
        return  firstleft
# Runtime: 36 ms, faster than 90.75% of Python3 online submissions for Partition List.
#Memory Usage: 14 MB, less than 5.05% of Python3 online submissions for Partition List.      