class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, maxcount = 0, 0
        for i in nums:
            if i == 1:
                count = count + 1
            else:
                maxcount = max(count, maxcount)
                count = 0

        maxcount = max(count, maxcount)     
        return maxcount