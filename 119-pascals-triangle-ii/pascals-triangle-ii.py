import math
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        '''
        1. deduced that the formula is nCr where n is the rowIndex and r is the index i
        2. for O(rowIndex) space complexity, if you deduce the formula, then there is no need to 
            come calculating from the top. so you can simply define a 1D list of 1s and only change values
            from index 1 to rowIndex-1

        '''

        triangle = [1] * (rowIndex+1)
        if rowIndex < 2:
            return triangle
        
        for i in range(1,rowIndex):
            triangle[i] = math.comb(rowIndex,i)
        return triangle

