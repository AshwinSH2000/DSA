class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        result = []
        other = set()
        for i in nums:
            if i not in other:
                other.add(i)
            else:
                result.append(i)
            
        return result
        