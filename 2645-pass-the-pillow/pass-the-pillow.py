class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        '''
        initial solution time complx: O(time)
        '''
        holding = 1
        direction = -1
        while time>0:
            if holding==n or holding==1:
                direction *= -1
            holding += direction
            time -= 1

        return holding