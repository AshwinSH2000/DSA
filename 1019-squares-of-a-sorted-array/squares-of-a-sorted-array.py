class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sq_arr = []
        for i in nums:
            sq_arr.append(i*i)
        sq_arr.sort()
        return sq_arr