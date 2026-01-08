class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        step = [0] * (len(cost)+1)
        cost.append(0)
        step[0] = cost[0]
        step[1] = cost[1]

        for i in range(2, len(cost)):
            step[i] = cost[i] + min(step[i-1],step[i-2])

        print(step)
        return step[len(cost)-1]