class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        '''
        you do not need to actually travel the points and then figure out. 
        instead, you can do it by just calculating the distance between them. 
        think how?
        '''
        seconds = 0
        for i in range(len(points)-1):
            seconds += max( abs(points[i][0]-points[i+1][0]), abs(points[i][1]-points[i+1][1]) )

        return seconds