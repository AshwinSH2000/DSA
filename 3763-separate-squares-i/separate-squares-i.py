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
                if square[1]+square[2] <= midY:
                    total_area += square[2]*square[2]
                elif square[1] <= midY and square[1]+square[2] > midY:
                    total_area += square[2]* (midY-square[1])
                # else: #square[1] > midY:
                    # total_area += 0 #because it is above the midY
                
            return total_area

        TOTAL = 0
        minY, maxY = float("inf"), 0
        midY = 0
        for square in squares:
            TOTAL += (square[2]*square[2])
            if square[1]<minY:
                minY = square[1]
            if (square[1]+square[2])>maxY:
                maxY = (square[1]+square[2])
            
        HALF_TOTAL = TOTAL/2
        
        while(maxY-minY>=0.00001):
            midY = (maxY+minY)/2
            cur_area = area(midY)
            if cur_area >= HALF_TOTAL:
                maxY = midY
            elif cur_area < HALF_TOTAL:
                minY = midY
            
        return midY

        



        