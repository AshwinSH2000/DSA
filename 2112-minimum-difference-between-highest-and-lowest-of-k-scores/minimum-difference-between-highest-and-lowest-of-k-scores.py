class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        '''
        sort the array and apply sliding window pattern
        since you have already sorted, the min and max will always be the first 
        element of the window and the last element of the window respectively.
        so you only need to find its difference and compare it with old difference.
        simply shortened the code, lol. check below comment for better understanding.
        '''

        nums.sort()
        minDiff = nums[k-1]-nums[0]
        for i in range(1, len(nums)-k+1):
            minDiff = min(minDiff, nums[i+(k-1)]-nums[i])
        return minDiff

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
        '''
        
        
        
