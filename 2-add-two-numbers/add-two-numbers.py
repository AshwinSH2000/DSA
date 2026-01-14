# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
    wrote this code without thinking much about the most efficient way. 
    wanted to get the working solution first. 
'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = [], []
        while l1 != None:
            n1.append(l1.val)
            l1 = l1.next

        while l2 != None:
            n2.append(l2.val)
            l2 = l2.next

        n1=n1[::-1]
        n2=n2[::-1]
        num1, num2 = 0, 0
        for i in range(len(n1)):
            num1 = num1*10 + n1[i]
        
        for i in range(len(n2)):
            num2 = num2*10 + n2[i]

        res = num1+num2
        if res == 0:
            return ListNode(0)
        res_head = ListNode()
        head = res_head
        print(res_head)
        while res > 0:
            temp = ListNode(res%10)
            if res_head is None:
                res_head = temp
            else:
                res_head.next = temp
                res_head = res_head.next
            res = res // 10

        return head.next

'''
        what should happen?
        1. create a header called res_head
        2. enter a while loop
        3. create a temp node
        4. append it to the end of res_head
        5. move res_head to its next node
        ...
        7. at the end return the actial starting point
'''