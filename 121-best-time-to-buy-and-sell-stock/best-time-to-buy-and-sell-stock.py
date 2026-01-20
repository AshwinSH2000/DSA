class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        had a list initially, later figured out that is unnecessary. 
        a simple variable is enough to track the profit.
        check diff to understand the changes
        '''
        n = len(prices)
        profit = 0
        bought = 0

        for i in range(1, n):
            profit = max(profit, prices[i]-prices[bought])
            if prices[i]<prices[bought]:
                bought = i

            
        return profit