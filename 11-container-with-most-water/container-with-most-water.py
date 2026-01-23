class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        two pointer approach. one on the ledt and another on the right. 
        calc area and store it. then move the lower value among the two 
        calc area and update if it is > max and keep doing until left<right
        '''
        n = len(height)
        if n==2:
            return min(height)
        
        left, right = 0, n-1
        maxarea = 0
        area = 0
        while left<right:
            area = (right-left)*min(height[left],height[right]) 
            maxarea = max(maxarea, area)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        
        return maxarea