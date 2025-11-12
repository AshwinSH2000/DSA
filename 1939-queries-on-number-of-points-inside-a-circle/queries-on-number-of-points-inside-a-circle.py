class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        result = [0 for i in queries]
        pt = 0
        for i in queries:
            for j in points:
                if (i[1]-j[1])**2 + (i[0]-j[0])**2 <= i[2]**2:
                    result[pt]+=1

            pt+=1
        return result