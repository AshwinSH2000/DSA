class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        '''
        staircase method. start off from the bottom left corner and move up
        each element has two options:
            i. it is -ve: then all elems to the right are -ve. hence move upwards
            ii. it is +ve: elems right may be -ve. hence move right

        '''
        sr, sc = len(grid) - 1, 0
        max_sc = len(grid[0])
        count = 0
        while sr >= 0 and sc < max_sc:
            if grid[sr][sc]<0:
                count = count + (max_sc - sc)
                sr = sr - 1 # moving up
            else:   
                sc = sc + 1 # moving right

        return count