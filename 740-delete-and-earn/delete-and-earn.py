class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        '''
        first, make an aggregated array from the given nums
        '''

        if len(nums) == 1:
            return nums[0]
        

        # there might be some easier code for the below agregation but
        # the thrill of writing it on my own is nice
        # but will update with a better method coz in intv, cant do this :p
        agg = {}
        for i in nums:
            if i in agg:
                agg[i] += 1
            else:
                agg[i] = 1

        a = set(agg.keys())
        agg_nums = [0] * (max(a)+1)
        for i in range(1, len(agg_nums)):
            if i in a:
                agg_nums[i] = i * agg[i]

        # once i get this array, then it reduces to the house robber problem
        n = len(agg_nums)
        dp = [0] * n
        dp[0] = agg_nums[0]
        dp[1] = agg_nums[1]

        for i in range(2, n):
            # now u either delete it and add points or skip and check for max
            dp[i] = max(agg_nums[i]+dp[i-2], dp[i-1])
        
        return dp[n-1]


        # remember that if len(nums)==2, you cant simply return max(nums[0], nums[1]). why?

