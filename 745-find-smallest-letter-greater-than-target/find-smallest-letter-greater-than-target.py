class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        '''
        im seriously confused looking at this... this qs in leetcode?
        but coded the linear search and submitted. got accepted. 
        then looked at topics. it mentioned binary search. realised i need to reduce TC
        then wrote binary search
        '''
        #binary search
        first, last = 0, len(letters)-1

        while(first<=last):
            mid = (first+last)//2

            if letters[mid]<=target:
                # letter match aadre, go to the right
                # because you need to return a letter that is greater than target.
                first = mid + 1
            else:
                last = mid - 1
            
        return letters[first % len(letters)]

        '''
        #linear search
        for char in letters:
            if char > target:
                return char
            
        return letters[0]
        '''