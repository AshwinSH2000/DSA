class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)//2
        dtn = {}
        for i in nums:
            if i not in dtn:
                dtn[i] = 1
            else:
                # dtn[i] = dtn[i] + 1
                # if dtn[i] == n:
                return i

         