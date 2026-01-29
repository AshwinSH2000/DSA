class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        learnt that we need to shallow copy the list here.
        simply appending list to res will be pass by reference.
        '''
        result = []
        n = len(nums)
        visited = [False] * n
        
        def permu(path):
            if len(path)==n:
                result.append(path[:])
                return

            for i in range(n):

                if visited[i]==True:
                    continue
                
                visited[i] = True
                path.append(nums[i])

                permu(path)

                path.pop()
                visited[i] = False

        permu([])
        return result
            

        