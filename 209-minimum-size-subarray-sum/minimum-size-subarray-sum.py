class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        min_length = float('inf') # given nums.length <= 10^5
        Sum = nums[0]
        while right < len(nums):
            if Sum >= target:
                min_length = min(min_length, right-left+1)
                Sum-=nums[left]
                left+=1
                if left>right:
                    right = left

            else:
                right+=1
                if right<len(nums):
                    Sum+=nums[right]

        return min_length if min_length != float('inf') else 0
       