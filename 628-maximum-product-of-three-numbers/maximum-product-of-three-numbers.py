class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        #im too tired today, and a very long day. hence picked this easy prob and used this approach. will come back later and try to improve it if its not optimal
        if len(nums)>3:
            nums.sort()

        return max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])