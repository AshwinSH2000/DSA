class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
        #set create maadbeku for every 3 chars. 
        #so aaga, if the length is 3, then goodSubStr +=1..gottait

        left = 0
        count = 0

        for right in range (2, len(s)):
            if len(set( s[left:right+1] )) == 3:
                count += 1
            
            left += 1
        return count

        