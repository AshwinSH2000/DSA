class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        remember the three types of backtracking problems?
        1. the permutations of given number.. over there yu use visited array to keep track of all remaining elements to choose from 
        2. this problem depends on position because the char associated with first digit can only come in the first place; second digit in the second place and so on. so you need to just keep track of position
        3. last type is combinations of some numbers. over there you need to keep track of index and start pos.
        '''
        hashMap = {'2':['a','b','c'], 
                   '3':['d','e','f'],
                   '4':['g','h','i'],
                   '5':['j','k','l'],
                   '6':['m','n','o'],
                   '7':['p','q','r','s'],
                   '8':['t','u','v'],
                   '9':['w','x','y','z']}

        # ignoring 1 in the hashmap as valid ip is from 2 to 9 incl.
        result = []
        def permute(path, index):
            if index == len(digits):
                result.append(path[:])  # remember pass by value & pass by reference
                return

            for letter in hashMap[digits[index]]:
                # choose letter in path
                # backtrack with the path and index + 1
                # discard the letter to try new one

                permute(path+letter, index+1)
                    


        permute("", 0)
        return result



