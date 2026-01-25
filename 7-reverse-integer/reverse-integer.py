class Solution:
    def reverse(self, x: int) -> int:

        answer = 0
        neg = True if x < 0 else False
        x = abs(x)
        
        while x > 0:
            rem = x % 10
            answer = answer*10 + rem
            x = x // 10

        if neg:
            answer *= -1
        
        if -2**31 <= answer <= (2**31 -1):
            return answer
        return 0
        

        