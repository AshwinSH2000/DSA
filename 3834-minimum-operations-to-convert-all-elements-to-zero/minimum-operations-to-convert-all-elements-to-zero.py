class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = []
        ops = 0

        for n in nums:
             
            while stack and stack[-1]>n:
                stack.pop()

            if n==0:
                continue

            if not stack or n>stack[-1]:
                ops += 1
                stack.append(n)

        return ops