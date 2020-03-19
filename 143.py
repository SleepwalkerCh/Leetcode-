# 143. Reorder List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        self.head=head
        self.new=ListNode(0)
        self.newhead=self.new
    def reverse(self,head):
        if head==None:
            return 
        else:
            self.reverse(head.next)
            self.newhead.next=head