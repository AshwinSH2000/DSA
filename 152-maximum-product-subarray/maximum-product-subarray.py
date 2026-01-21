class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        Slightly modified kadane's algorithn. You need to keep track of both min and max products
        so at each index, you need to figure out if the max product is max of ( new subarray starting at that index, prev maxprod * that index, prev minprod * that index) - the last case is true when your minprod was a -ve number and the current number is a negative number which makes the product positive and it can turn out to be a max positive number
        
        similarly, at this step you noticed that minprod can help you find the maxprod. which makes it essential to even calculate the minprod. at this step, you find the minpd is equal to minimum of (new subarray starting at that point, previous maxprod * that index, previous minprod * that index). 
        Because of negative numbers, the prev minprod can become maxprod and preev maxprod can become minprod. Also used temp because maxprod interferes with calculations and produces wrong maxprod otherwise. 
        
        '''
        min_prod = nums[0]
        max_prod = nums[0]
        maxProdSubarray = nums[0]

        for i in range(1, len(nums)):
            temp = max(nums[i], max_prod*nums[i], min_prod*nums[i])
            min_prod = min(nums[i], max_prod*nums[i], min_prod*nums[i])
            max_prod = temp

            maxProdSubarray = max(maxProdSubarray, max_prod)

        return maxProdSubarray
            