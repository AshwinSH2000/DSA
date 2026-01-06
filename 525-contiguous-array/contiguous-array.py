class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        '''
        ok so the funda is add 1 when it is 1 and subtract 1 when it is 0
        keep track of the earliest unique prefixSum
        whenever you encounter the same prefix sum again, compute the length
        store greater 
        '''
        prSum = 0
        hashmap = {0:-1} #this is imp. for example 1
        longest = 0

        for i in range(len(nums)):
            if nums[i]:
                prSum += 1
            else:
                prSum -= 1

            if prSum not in hashmap:
                hashmap[prSum] = i
            else:
                # hashmap[prSum] = min(i, hashmap[prSum])
                longest = max(longest, i - hashmap[prSum])

        print(hashmap)
        return longest
