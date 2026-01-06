class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        use a hashmap to store all the previous prefix sums
        then check if key current_sum - k exists in the hashmap
        increment the count with its value
        '''
        prevSumMap = {0: 1}
        runningSum = 0
        count = 0
        for i in nums:
            runningSum += i
            if (runningSum - k) in prevSumMap:
                count += prevSumMap[runningSum - k]
                
            if runningSum in prevSumMap:
                prevSumMap[runningSum] += 1
            else:
                prevSumMap[runningSum] = 1

        return count
        