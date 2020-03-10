#160. Intersection of Two Linked Lists
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lengtha,lengthb=0,0
        a,b=headA,headB
        while a!=None:
            a=a.next
            lengtha+=1
        while b!=None:
            b=b.next
            lengthb+=1
        if lengtha>lengthb:
            for i in range(lengtha-lengthb):
                headA=headA.next
        else:
            for i in range(lengthb-lengtha):
                headB=headB.next
        while headA!=None and headA!=headB:
            headA=headA.next
            headB=headB.next
        if headA!=None:
            return headA
        else:
            return None
#Runtime: 292 ms, faster than 5.18% of Python3 online submissions for Intersection of Two Linked Lists.
#Memory Usage: 27.9 MB, less than 100.00% of Python3 online submissions for Intersection of Two Linked Lists.