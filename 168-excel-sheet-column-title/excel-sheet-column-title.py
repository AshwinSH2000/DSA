class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        '''
        one niche point here
        for the least significant bit, you can do mod 26 but the issue is
        for A you do mod 26 and get remainder 1 
        but when it reaches Z, you do mod 26 and you get 0
        (A to Y you can simply add it to ord('A') but for Z it becomes a problem)
        so now when you do num-1, entire sequence gets taken care of. how?
        A will be ord(A)+0 and Z will be ord(A)+25
        
        
        '''

        output = ""
        while columnNumber > 0:
            columnNumber -= 1 # this is the imp part to account for Z only
            remainder = columnNumber % 26
            output = chr(ord('A')+remainder) + output 
            columnNumber = columnNumber // 26

        return output
       
            