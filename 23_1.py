#23. Merge k Sorted Lists
#太慢了，记录非空的ListNode编号，对最小值进行归并
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isNullList(self,lists: List[ListNode])-> bool:
        for i in lists:
            if i:
                return False
        return True
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        new=ListNode(-1)
        head=new
        listbool=[]
        for i in range(len(lists)):
            if lists[i]:
                listbool.append(i)
        while listbool:
            min=lists[listbool[0]].val
            nmin=listbool[0]
            imin=0
            for i in range(len(listbool)):
                if lists[listbool[i]].val<=min:
                    min=lists[listbool[i]].val
                    nmin=listbool[i]
                    imin=i
            new.next=lists[nmin]
            new=new.next
            lists[nmin]=lists[nmin].next
            if not lists[nmin]:
                del listbool[imin]
        return head.next
#Runtime: 4720 ms, faster than 10.35% of Python3 online submissions for Merge k Sorted Lists.
#Memory Usage: 16.2 MB, less than 96.07% of Python3 online submissions for Merge k Sorted Lists.
