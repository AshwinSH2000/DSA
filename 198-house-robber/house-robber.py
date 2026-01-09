class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        you can start from house 0 or 1
        but need not rob every other house... 
        need to see which gives more money
        unlike climbing stairs, you can choose to ignore some houses(steps)

        here dp[i] represents the max money i can steal from homes 0...i
        '''
        
        n = len(nums)
        if n==1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        for i in range(2, n):
            dp[i] = max(nums[i]+dp[i-2], dp[i-1])

        return dp[n-1]