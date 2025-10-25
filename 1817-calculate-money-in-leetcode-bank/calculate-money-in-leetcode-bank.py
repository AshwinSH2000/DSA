class Solution:
    def totalMoney(self, n: int) -> int:
       # O(1) approach---------------------------- 
        weeks = n // 7
        days = n % 7
        #the above can be replaced by weeks, days = divmod(n, 7)
        total = (28*weeks) + (7 * weeks * (weeks-1)//2 ) + (days*(days+1)//2) + days*weeks
        return total
        # O(1) approach----------------------------

        # O(N) approach----------------------------
        # days = 1
        # money = 0
        # week = 0
        # while days <= n:

        #     money = money + (days % 7) + week

        #     if days % 7 == 0:
        #         week+=1
        #         money += 7

        #     days += 1
        
        # return money
        # O(N) approach----------------------------

            

         