# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        else:
            prev, curr, nex = head, head.next, head.next.next
            
            while curr is not None:
                curr.next = prev
                prev = curr
                curr = nex
                if nex is not None:
                    nex = nex.next

            head.next = None
            head = prev
            return head