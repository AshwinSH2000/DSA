class Solution:
    def intToRoman(self, num: int) -> str:
        '''
        imp thing to note is the subtraction rules in roman numerals.
        1. you can only subtract one number at a time. (cant to IIV or IIX)
        2. I can be subtracted from V and X only
        3. X can be subtracted from L and C only
        4. C can be subtracted from D and M only. 
        '''
        hashMap = {}

        d, r = divmod(num,1000)
        hashMap[1000]=d
        d, r = divmod(r,500)
        hashMap[500]=d
        d,r = divmod(r,100)
        hashMap[100] = d
        d,r = divmod(r,50)
        hashMap[50] = d
        d,r = divmod(r,10)
        hashMap[10] = d
        d,r = divmod(r,5)
        hashMap[5] = d
        hashMap[1] = r

        output = ""

        output += "M"*(hashMap[1000])
        
        if hashMap[100]<=3:
            output += "D"*(hashMap[500])
            output += "C" * hashMap[100]
        elif hashMap[500]==1 and hashMap[100]==4:
            output += "CM"
        else:
            output += "CD"

        if hashMap[10]<=3:
            output += "L"*hashMap[50]
            output += "X"*hashMap[10]
        elif hashMap[50]==1 and hashMap[10]==4:
            output += "XC"
        else:
            output += "XL"

        if hashMap[1]<=3:
            output += "V"*hashMap[5]
            output += "I"*hashMap[1]
        elif hashMap[5]==1 and hashMap[1]==4:
            output += "IX"
        else:
            output += "IV"
            
        return output
