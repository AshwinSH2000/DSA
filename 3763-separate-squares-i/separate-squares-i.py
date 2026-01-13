class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        """
        how to solve this?

        1. calc the total area and the min, max y values
        2. perform binary search between min and max y
        3. check if the area belwo the mid is equal to half the total area
        4. if it is, and if the different (high-low) is less than 10^5 brk and return

        """

        def area(midY):
            total_area = 0
            for square in squares:
                if square[1] + square[2] <= midY:
                    total_area += square[2] * square[2]
                elif square[1] <= midY and square[1] + square[2] > midY:
                    total_area += square[2] * (midY - square[1])

            return total_area

        TOTAL = 0
        minY, maxY = float("inf"), 0
        midY = 0
        for square in squares:
            TOTAL += square[2] * square[2]
            if square[1] < minY:
                minY = square[1]
            if (square[1] + square[2]) > maxY:
                maxY = square[1] + square[2]

        HALF_TOTAL = TOTAL / 2

        while maxY - minY >= 0.00001:
            midY = (maxY + minY) / 2
            cur_area = area(midY)
            if cur_area >= HALF_TOTAL:  # why is it >= ... think
                maxY = midY
            else:
                minY = midY

        return midY

        """
        its >= in line 38 because, even if the cur_area == HALF_TOTAL, 
        we want to bring the midY line down. 
        Yes, when the two areas are equal, midY is exactly (minY+maxY)/2 but 
        remember in the first example, it is shown very well. 
        the exact midY is 1.5 but we need to choose the min value of all possible y. 
        so the minimum value is 1. to help with this calculation, we choose >= 
        """
