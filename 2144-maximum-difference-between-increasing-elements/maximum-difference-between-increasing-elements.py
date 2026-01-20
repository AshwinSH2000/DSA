class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        maxdiff = 0

        for j in range(n):
            if nums[j] < nums[i]:
                i = j

            maxdiff = max(maxdiff, nums[j] - nums[i])

        return -1 if maxdiff == 0 else maxdiff
