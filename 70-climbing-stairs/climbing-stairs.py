class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        basic idntfn: step[n] = step[n-1]+step[n-2]
        the no of ways to reach n step is either a final 1 step jump from n-1
        or a two step jump from n-2
        '''

        if n == 1 or n == 0:
            return 1
        
        step = [0] * (n+1)
        step[0] = 1
        step[1] = 1
        for i in range(2, n+1):
            step[i] = step[i-1] + step[i-2]
        
        print(step)
        return step[n]
        