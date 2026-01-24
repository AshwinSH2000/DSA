class Solution:
    def romanToInt(self, s: str) -> int:
        '''
        some rules in roman numerals
        1. can only subtract once consecutively in a number
        2. I can be subtracted from V and X only
        3. X can be subtracted from L and C only
        4. C can be subtracted from D and M only
        '''
        hashmap = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        result = 0
        prev = ""
        for i in range(len(s)-1, -1, -1):
            char = s[i]
            if char == "I":
                if prev == "V" or prev == "X":
                    result -= 1
                else:
                    result += hashmap[char]
            elif char == "X":
                if prev == "L" or prev == "C":
                    result -= 10
                else:
                    result += hashmap[char]
            elif char == "C":
                if prev == "D" or prev == "M":
                    result -= 100
                else:
                    result += hashmap[char]
            else:
                result += hashmap[char]

            prev = char

        return result

        
        