class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a)>len(b):
            b = "0" * (len(a)-len(b)) + b
        elif len(b)>len(a):
            a = "0" * (len(b)-len(a)) + a

        sumint = 0
        sum = ""
        carry = 0

        a = a[::-1]
        b = b[::-1]

        for i in range (len(a)):
            sumint = int(a[i]) + int(b[i]) + carry
            if sumint <= 1:
                sum += str(sumint)
                carry = 0
            elif sumint == 2:
                sum += "0"
                carry = 1
            elif sumint == 3:
                sum += "1"
                carry = 1
        
        if carry == 1:
            sum += str(carry) 

        sum = sum[::-1]
        return sum
