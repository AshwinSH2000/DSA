class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * n
        bought = 0

        for i in range(1, n):
            dp[i] = max(dp[i-1], prices[i]-prices[bought])
            if prices[i]<prices[bought]:
                bought = i

            
        return dp[n-1]