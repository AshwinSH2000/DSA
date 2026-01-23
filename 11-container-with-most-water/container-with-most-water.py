class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        two pointer approach. one on the ledt and another on the right. 
        calc area and store it. then move the lower value among the two 
        calc area and update if it is > max and keep doing until left<right
        '''
        
        left, right = 0, len(height)-1
        maxarea = 0
        while left<right:
            min_h = height[left]
            max_h = height[right]
            area = (right-left)*min(min_h,max_h) 
            maxarea = max(maxarea, area)
            if min_h<max_h:
                left+=1
            else:
                right-=1
        
        return maxarea