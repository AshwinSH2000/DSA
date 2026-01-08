class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        step = [0] * (n)
        step[0] = cost[0]
        step[1] = cost[1]

        for i in range(2, n):
            step[i] = cost[i] + min(step[i-1],step[i-2])

        return min(step[n-1], step[n-2])
        '''
        old approach... works but not so clean soln
        step = [0] * (len(cost)+1)
        cost.append(0)
        step[0] = cost[0]
        step[1] = cost[1]

        for i in range(2, len(cost)):
            step[i] = cost[i] + min(step[i-1],step[i-2])

        print(step)
        return step[len(cost)-1]
        '''