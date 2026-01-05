class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        divi = 100
        count = 0
        for i in nums:
            divi = 100
            while i >= 1:
                i = i/divi
                divi * 100

            if i>=0.1 and i<1:
                count = count + 1

        return count