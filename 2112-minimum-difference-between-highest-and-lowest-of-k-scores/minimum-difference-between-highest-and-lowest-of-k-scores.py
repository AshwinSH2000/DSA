class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        '''
        sort the array and apply sliding window pattern
        '''
        if k==1:
            return 0

        nums.sort()
        
        Min, Max = nums[0], nums[k-1]
        minDiff = Max-Min
        
        n = len(nums)
        for i in range(1, n-k+1):
            Min = nums[i]
            Max = nums[i+(k-1)]
            minDiff = min(minDiff, Max-Min)

        return minDiff

        
        
        
