class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)):
            nums[i] = nums[i]*nums[i]
        nums.sort()
        return nums
        # sq_arr = []
        # for i in nums:
        #     sq_arr.append(i*i)
        # sq_arr.sort()
        # return sq_arr