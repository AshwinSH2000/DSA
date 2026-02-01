class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        '''
        not exactly sure but this is what i thought within first 2 mins of seeing the problem
        we need to divide the array into three and its first element must add up to have a min val. 
        so my idea was to find the three min values and splice but that doesnt work in example 3. 
        so the change in plan was to include first element as is, then find the smallest two elems. 
        '''
        n = len(nums)
        if n == 3:
            return sum(nums)

        first = 0
        smallest = float(inf)
        second_smallest = float(inf)

        for i in range(1, n):
            if nums[i] <= smallest:
                second_smallest = smallest
                smallest = nums[i]
            elif nums[i] < second_smallest and nums[i] != smallest:
                second_smallest = nums[i]


        return nums[0]+smallest+second_smallest