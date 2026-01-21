class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        '''
        key thing to remember:
        when the product of any subarray is less than k, 
        then you count all possible subarrays in it. 
        '''
        product = 1
        left, right = 0, 0
        count = 0
        n = len(nums)  

        while right < n:
            product *= nums[right]
            
            while product >= k and left <= right :
                product /= nums[left]
                left +=1

            count += (right - left + 1)
            right += 1
        
        return count

        