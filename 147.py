# 147. Insertion Sort List
# 指针拼接
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:

        if head.next==None:
            return head
        headNode=ListNode(0)
        headNode.next=head
        i,ilast=head.next,head
        while i != None:
            j,jlast=head,headNode

            while j!=i:
                print(ilast.val,i.val,jlast.val,j.val)
                if j.val>=i.val:
                    jlast.next=i
                    ilast.next=i.next
                    i.next=j
                    break
                jlast=j
                j=j.next
            if j==i:
                ilast,i=i,i.next
                continue
            #ilast=i
            i=ilast.next
        return headNode.next
#Runtime: 1752 ms, faster than 41.25% of Python3 online submissions for Insertion Sort List.
#Memory Usage: 14.6 MB, less than 100.00% of Python3 online submissions for Insertion Sort List.