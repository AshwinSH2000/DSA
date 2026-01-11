class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        so conv, dp[n] is the max money i can steal from house 0 to n
        but it is cyclic here so need to check dp[0] when at dp[n]

        my logic of using % for cyclic op turned out to be wrong. why?
        in that approach, you will end up using the information of dp not yet calculated
        or in other words 'inf of the future' hence it breaks the principle of dp. 
        you use solutions of smaller/subproblems to solve larger problems but if you 
        approach cyclically, you end up using bigger solution to solve smaller prob. 
        artha aytha?
        so use 0 to n-1 and 1 to n and find max of that approach. 
        '''

        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        def house_robber(houses: List[int]) -> int:
            n = len(houses)
            if n==2:
                return max(houses[0], houses[1])
            
            dp = [0]*n
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])

            for i in range(2, n):
                dp[i] = max(houses[i]+dp[i-2], dp[i-1])
            
            return dp[n-1]

        return max( house_robber(nums[:-1]) , house_robber(nums[1:]) )

    