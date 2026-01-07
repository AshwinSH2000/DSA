class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        '''
        imp stt to understand here: (it is mentioned indirectly)
        prefix needs to start from index 0
        so if you have an array [1,3,4,5,6], the ans is 2
        how? longest sequential prefix is just 1.
        sum of the longest seq prefix is 1 but it is in nums
        hence return the smallest int greater than 1 that is not in nums i.e 2
        '''
        
        if len(nums)==1:
            return nums[0]+1
        
        prefixSum = nums[0]
        for i in range (1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                prefixSum += nums[i]
            else:
                break
            
        while prefixSum in nums:
            prefixSum += 1
        
        return prefixSum

        
