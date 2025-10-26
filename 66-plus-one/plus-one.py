class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #if the least sig digit is 9, then just need to update next sig digit
        #else just increment it and return

        if digits[-1] != 9:
            digits[-1]+=1
        else:
            rev = digits[::-1]
            carry = 0
            for i in range(len(rev)):
                if rev[i] == 9:
                    rev[i] = 0
                    carry = 1
                else:
                    rev[i] += carry
                    carry = 0
                    break

            if carry == 1:
                rev.append(carry)
            
            digits = rev[::-1]

        return digits
        