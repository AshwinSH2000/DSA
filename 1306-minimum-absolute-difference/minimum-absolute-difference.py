class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        '''
        the first approach that struck me
        sort it. so you only need to check adjacent elements for smallest difference
        once the min diff is found, search and note down all pairs that have mindiff
        '''
        arr.sort()
        n = len(arr)
        minDiff = float('inf')
        for i in range(n-1):
            minDiff = min(minDiff, arr[i+1]-arr[i])
        
        result = []
        for i in range(n-1):
            if (arr[i+1]-arr[i])==minDiff:
                result.append([arr[i], arr[i+1]])

        return result