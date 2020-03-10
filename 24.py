#24. Swap Nodes in Pairs
#直接对其两两对换即可
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def printListNode(self):
        Node=self
        while Node:
            print(Node.val)
            Node=Node.next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        if not head:
            return head
        else:
            one=head
            if not one.next:
                return head
            else:
                two=one.next
                nowhead=ListNode(0)
                head1=nowhead
                while one and two:
                    nowhead.next=two
                    one.next=two.next
                    two.next=one
                    nowhead=one
                    one=nowhead.next
                    if one:
                        two=one.next
                return head1.next
sol=Solution()
one=ListNode(1)
one.next=ListNode(2)
one.next.next=ListNode(3)
one.next.next.next=ListNode(4)
one.printListNode()
sol.swapPairs(one).printListNode()
                    

#Runtime: 32 ms, faster than 93.32% of Python3 online submissions for Swap Nodes in Pairs.
#Memory Usage: 13.1 MB, less than 82.06% of Python3 online submissions for Swap Nodes in Pairs.