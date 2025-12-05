class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n-1):
            if (sum(nums[:i+1])-sum(nums[i+1:]))%2==0:
                ans+=1

        return ans