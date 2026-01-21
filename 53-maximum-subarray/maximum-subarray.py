class Solution:
    '''
    Kadane's algorithm needs to be used
    So at a particular index, you decide if you need to start a new subarray
    or add the current value to the old subarray and continue it. 

    Here inside the loop, 1st line gives max sum by either starting a new subarray(and putting its value to maxEndingSum) or by continuing it(by adding nums[i] to the current value of maxEndingSum).
    and 2nd line gives max subarray sum from some old maxSubarraySum or newest subarray which we just saw.
    '''
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxSubarraySum = nums[0]
        maxEndingSum = nums[0]
        for i in range(1, len(nums)):
            maxEndingSum = max(nums[i], maxEndingSum+nums[i])
            maxSubarraySum = max(maxSubarraySum, maxEndingSum)

        return maxSubarraySum