#92. Reverse Linked List II
#借用25题的reverse思路
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        
        self.n=n
        forward=ListNode(0)
        forward.next=head
        first=forward
        for i in range(m-1):
            forward=head
            head=head.next
        self.tail=None
        self.Reverse(forward,forward,head,m)
        head.next=self.tail
        return first.next
    def Reverse(self,cur,forward,now,num):#cur之前头部，forward前指针，now现指针，num计数
        if num==self.n:
            cur.next=now
            self.tail=now.next
            now.next=forward       
            return num
        else:
            if now.next==None:
                return -1
            if self.Reverse(cur,now,now.next,num+1)!=-1:
                now.next=forward
            else:
                return -1
            return num