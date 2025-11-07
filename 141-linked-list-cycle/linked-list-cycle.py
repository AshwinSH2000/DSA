class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # this problem needs fast and slow pointers... oki got it!

        fastPtr = head
        while fastPtr and fastPtr.next:
            fastPtr = fastPtr.next.next
            head = head.next

            if head == fastPtr:
                return True

        return False
