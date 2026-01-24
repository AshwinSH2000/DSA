class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        first, last = 0, n-1
        maxPairSum = 0
        while first<last:
            Sum = nums[first]+nums[last]
            maxPairSum = max(maxPairSum, Sum)
            first += 1
            last -= 1

        return maxPairSum