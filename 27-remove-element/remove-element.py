class Solution(object):
    def removeElement(self, nums, val):
        i, j = 0, len(nums)-1
        while(i<j):
            if nums[i]==val:
                if nums[j]==val:
                    j-=1
                else:
                    nums[i], nums[j] = nums[j], nums[i]
                    i+=1
                    j-=1
            else:
                i+=1
        if (i==j and nums[i]==val) or (i>j):
            return i
        else:
            return i+1