class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        appleSum = sum(apple)
        m = len(capacity)
        sumCap=0
        for i in range (m):
            sumCap = sumCap + capacity[i]
            if appleSum <= sumCap:
                return i+1

        return 0
