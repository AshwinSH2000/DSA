class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        logic behind this
        have two independent loops and find the prefix and suffix products: O(n)
        in the third iteration, to find the product of array w/o num, multiply its
        prefix sum to from its left side and its suffix sum from its right side
        '''
        n = len(nums)
        prefixSum = []
        suffixSum = [0]*n
        
        for i in range(n):
            if not i:
                prefixSum.append(nums[i])
            else:
                prefixSum.append(nums[i]*prefixSum[i-1])

        for i in range(n-1, -1, -1):
            if i==n-1:
                suffixSum[i]=nums[i]
            else:
                suffixSum[i]=(nums[i]*suffixSum[i+1])

        # ok now need to find the product of left and right
        result = []
        for i in range(n):
            if i==0:
                result.append(suffixSum[i+1])
            elif i==n-1:
                result.append(prefixSum[i-1])
            else:
                result.append(prefixSum[i-1]*suffixSum[i+1])
        
        return result