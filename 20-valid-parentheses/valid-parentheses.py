class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for i in s:
            if i in "{[(":
                stk.append(i)
            elif not stk and i in "]})":
                return False
            
            elif i == "]":
                if stk.pop() != "[":
                    return False
            elif i == "}":
                if stk.pop() != "{":
                    return False
            elif i == ")":
                if stk.pop() != "(":
                    return False
            
        if stk == []:
            return True
        return False
        