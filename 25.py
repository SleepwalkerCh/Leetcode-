#25. Reverse Nodes in k-Group
# 回溯从后往前调换顺序
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        first=ListNode(0)
        first.next=head
        cur=first
        self.k=k
        while head:
            if not head.next:
                break
            if self.Reverse(cur,head,head.next,2)==-1:
                return first.next
            else:
                head.next=self.tail
                cur=head
                head=cur.next

        return first.next
    def Reverse(self,cur,forward,now,num):
        if num==self.k:
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



#Runtime: 56 ms, faster than 57.28% of Python3 online submissions for Reverse Nodes in k-Group.
#Memory Usage: 15.5 MB, less than 5.00% of Python3 online submissions for Reverse Nodes in k-Group.