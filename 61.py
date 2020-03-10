#61. Rotate List
#接头续尾
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        flag=head
        num=1
        if head==None:
            return None
        while flag.next!=None:
            num+=1
            flag=flag.next
        if num==1:
            return head
        elif k%num==0:
            return head
        i=0
        flag2=head
        while i<(num-k-1) % num:
            flag2=flag2.next
            i+=1
        res=flag2.next
        flag.next=head
        flag2.next=None
        return res
#Runtime: 36 ms, faster than 93.71% of Python3 online submissions for Rotate List.
#Memory Usage: 13.9 MB, less than 5.24% of Python3 online submissions for Rotate List.