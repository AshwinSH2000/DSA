class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        left, right = 0,0
        n = len(colors)
        sumTime = 0
        maxTime = 0
        ans=0
        while right+1<=n:

            if colors[left]==colors[right]:
                sumTime += neededTime[right]
                maxTime = max(maxTime, neededTime[right])
                right += 1
            if right==n or colors[left]!=colors[right]:
                ans+=(sumTime-maxTime)
                left = right
                sumTime = 0
                maxTime = 0

        if right+1==n:
            ans+=(sumTime-maxTime)
        return ans

            
             

