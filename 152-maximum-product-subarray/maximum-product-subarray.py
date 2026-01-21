class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_prod = nums[0]
        max_prod = nums[0]
        maxProdSubarray = nums[0]

        for i in range(1, len(nums)):
            temp = max(nums[i], max_prod*nums[i], min_prod*nums[i])
            min_prod = min(nums[i], max_prod*nums[i], min_prod*nums[i])
            max_prod = temp

            maxProdSubarray = max(maxProdSubarray, max_prod)

        return maxProdSubarray
            