class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        prefix = "" #keep an empty string as prefix
        letter = 0
        end = False
        char = ""
        while (True):
            #break when the char doesnt match or word ends
            for i in range (len(strs)):
                try:
                    if(strs[i][letter]):
                        char = strs[0][letter]
                        #if the letter exists, check if it matches
                        if(strs[i][letter]!=char):
                            #if it doesnt match, break
                            end = True
                            break

                except:
                    end = True
                    break
            if(end == True):
                break  
               
            prefix += strs[0][letter]
            letter+=1
        return prefix