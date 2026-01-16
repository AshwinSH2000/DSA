class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        '''
        you perform runningsum%k and check if that remainder is present in hashmap
        if it is present, check its value(aka index, in this qs)
            if the indices difference >=2, then its a good subarray ; return true
        store the remainder and its index in hashmap for future reference. 

        thing to keep in mind: what if the first element is itself multiple of k
        '''
        
        prevSum = {0:-1} 
        runningSum = 0
        for i in range(len(nums)):
            runningSum += nums[i]
            rem = runningSum % k
            if rem in prevSum:
                if i-prevSum[rem]>=2:
                    return True
            else:
                prevSum[rem] = i

        return False
