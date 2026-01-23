class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        """
        i initially had an idea and i asked chatgpt if its the right approach. it said no.
        i asked for some evidence and it gave 4 examples and all 4 were wrong. my approach was
        working in all of them. hence i coded it here and submitted the same.
        found the bug. it fails for this test case: [8,6,3,13,2,12,19,5,19,6,10,11,9]
        however, i will just comment my code and go for the optimised approach.
        i will need it to remember later what NOT to do!

        the correct approach is to find a max value on either side for every possible j.
        then caculate the value and keep track with the max value
        """
        n = len(nums)
        maxValue = 0
        prefixMax = [0] * n
        prefixMax[0] = nums[0]
        suffixMax = [0] * n
        suffixMax[n-1] = nums[n-1]

        for i in range(1, len(nums)):
            prefixMax[i] = max(prefixMax[i-1], nums[i])
        
        for i in range(n-2, -1, -1):
            suffixMax[i] = max(suffixMax[i+1], nums[i])

        # prefixMax[i] is the max from 0 to i. so in the below loop, 
        # we need to use only prefixMax[index-1]
        # similarly, we need to use only suffixMax[index+1] 
        # suffixMax[i] includes max from i to end
        for index in range(1, len(nums) - 1):
            i = prefixMax[index-1]
            j = nums[index]
            k = suffixMax[index+1]

            maxValue = max(maxValue, (i - j) * k)

        return maxValue

        # j = nums.index(min(nums))
        # while j==0 or j==(len(nums)-1):
        #     if j==0:
        #         nums = nums[1:]
        #     else:
        #         nums = nums[:len(nums)-1]
        #     if nums:
        #         j = nums.index(min(nums))
        #     else:
        #         break

        # if not nums:
        #     return 0

        # i = nums.index(max(nums[:j]))
        # k = nums.index(max(nums[j+1:]))

        # return (nums[i]-nums[j])*nums[k]
