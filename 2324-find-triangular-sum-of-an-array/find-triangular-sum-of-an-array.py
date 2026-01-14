class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        '''
        feels a straightforward question.
        just remember to initialise the newNums inside the while loop
        '''
        while len(nums) > 1:
            newNums = []
            for i in range(len(nums)-1):
                newNums.append((nums[i]+nums[i+1])%10)
            nums = newNums

        return nums[0]