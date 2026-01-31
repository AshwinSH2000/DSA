class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        '''
        im seriously confused looking at this... this qs in leetcode?
        but coded the linear search and submitted. 
        '''
        for char in letters:
            if char > target:
                return char
            
        return letters[0]