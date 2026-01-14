import math
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = [1] * (rowIndex+1)
        if rowIndex < 2:
            return triangle
        
        for i in range(1,rowIndex):
            triangle[i] = math.comb(rowIndex,i)
        return triangle