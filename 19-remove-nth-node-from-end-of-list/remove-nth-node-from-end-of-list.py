# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        the first thing i had in mind is that it requires two passes
        le question at the end: do it in one pass
        me: :(

        ok anyhow first i am trying to do it in two passes
        '''
        sz = 0
        temp_head = head

        while(temp_head is not None):
            temp_head = temp_head.next
            sz+=1
        
        if sz==n:           #this means i have to delete the first node itself. 
            return head.next

        temp_head = head
        while(temp_head is not None):
            if sz==n+1:
                temp_head.next = temp_head.next.next
                break
            sz-=1
            temp_head = temp_head.next
        return head
            