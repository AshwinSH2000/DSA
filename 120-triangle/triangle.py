class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        def get(i: int, j:int) -> int:
            if 0 <= j <= i:
                return triangle[i][j]
            return float('inf')
            '''
            i had these 4 lines of code in the function. 
            they were mostly fine but gave errors because i expected tr[x][-1] to give error
            but it instead picked the last element of xth row. i knew this property but
            didnt think when i was coding it.
            try:
                return triangle[i][j]
            except:
                return float('inf')
            '''
        
        for i in range(1, len(triangle)):
            for j in range(0,i+1):
                print(triangle[i][j], get(i-1,j), get(i-1, j-1))
                triangle[i][j] = triangle[i][j] + min(get(i-1, j), get(i-1,j-1))

        print(triangle)   
        return min(triangle[len(triangle)-1])

            
            
