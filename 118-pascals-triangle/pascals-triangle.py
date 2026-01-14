class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        [1]                     i=0 j<=0
        [1,1]                   i=1 j<=1
        [1,2,1]                 i=2 j<=2    for [2][1] it is [1][0]+[1][1]
        [1,3,3,1]               i=3 j<=3    for [3][1] it is [2][0]+[2][1] and for [3][2] it is [2][1]+[2][2]
        [1,4,6,4,1]             i=4 j<=4
        [1,5,10,10,5,1]         i=5 j<=5
        [1,6,15,20,15,6,1]      i=6 j<=6
        so the pattern is fill 1 for j=0 and j=i and for other j values, it is arr[i-1][j-1]+arr[i-1][j]
        """
        triangle = []
        for i in range(numRows):
            row = []
            for j in range(i + 1):
                if j == i or j == 0:
                    row.append(1)
                else:
                    row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            triangle.append(row)

        return triangle
