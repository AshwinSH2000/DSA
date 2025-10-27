class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s==s[::-1]:
            return True
        else:
            i, j=0, len(s)-1
            while (i<=j):
                if s[i]==s[j]:
                    i+=1
                    j-=1
                else:
                    word1 = s[:i]+s[i+1:]
                    word2 = s[:j]+s[j+1:]

                    if word1==word1[::-1] or word2==word2[::-1]:
                        return True
                    else:
                        return False

            

        