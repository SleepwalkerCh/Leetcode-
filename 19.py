#19. Remove Nth Node From End of List
#两个指针之间固定步长，一次遍历即可完成题目要求

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        Point1=head
        Point2=head
        for i in range(n):
            Point1=Point1.next
        if not Point1:
            return head.next
        else:
            while Point1.next:
                Point1=Point1.next
                Point2=Point2.next
            Point2.next=Point2.next.next
            return head