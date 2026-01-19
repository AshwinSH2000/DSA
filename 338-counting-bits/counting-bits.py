class Solution:
    def countBits(self, n: int) -> List[int]:
        '''
        if the number is 2^i, then ans is 1
        for all other numbers, ans is 1 + dp[i-largest 2^i seen before]
        i had initially thought to check if i is 2^i but the below has a nice 
        alternative way of writing it
        '''
        last = 1
        dp = [0] * (n+1) #given

        for i in range(1, n+1):
            if i == last*2:
                last *= 2
            dp[i] = 1+ dp[i-last]

        return dp
        
            