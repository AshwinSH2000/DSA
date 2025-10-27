class Solution:
    def isPalindrome(self, s: str) -> bool:
        news = ""
        for i in s:
            if i.isalnum():
                news+=i.lower()
            
        return news == news[::-1]
        # version 1
        # newstr1 = ""
        # newstr2 = ""
        # i, j =0, len(s)-1

        # while(i != len(s) and j != -1):
        #     if s[i].isalnum() == True:
        #         newstr1 += s[i].lower()
        #     if s[j].isalnum() == True:
        #         newstr2 += s[j].lower()
        #     i+=1 
        #     j-=1
        # print(newstr1)
        # print(newstr2)
        # if newstr1 == newstr2:
        #     return True
        # else:
        #     return False
        # version 1


        

        