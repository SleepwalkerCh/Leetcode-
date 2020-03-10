#142. Linked List Cycle II
# 使用了额外存储 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fp,sp=head,head
        circleList=[]
        circleHead=None
        while fp and sp and fp.next and fp.next.next and sp.next:
            fp=fp.next.next
            sp=sp.next
            if fp==sp:
                circleHead=fp
                break
        if circleHead==None:
            return None
        circleList.append(circleHead)
        fp=fp.next
        while fp!=circleHead:
            circleList.append(fp)
            fp=fp.next
        while not head in circleList:
            head=head.next
        return head
#Runtime: 200 ms, faster than 5.64% of Python3 online submissions for Linked List Cycle II.
#Memory Usage: 16 MB, less than 100.00% of Python3 online submissions for Linked List Cycle II.