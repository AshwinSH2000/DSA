class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        '''
        coming from solving 169. Excel sheel column name
        so my immediate approach is to go the opposite way maybe?
        start from the right calculate the difference between the char and ord(A) and add 1 to it. 
        for each new left char, multiply the difference with 26^i where i is the pos from right (LSB is pos 0)
        remember that [::-1] is not in place! 
        '''

        result = 0
        columnTitle = columnTitle[::-1]

        for i in range(len(columnTitle)):
            difference = ord(columnTitle[i])-ord('A')+1
            result = result + pow(26,i)*difference

        return result