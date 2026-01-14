class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        leftsum = 0
        rightsum = sum(nums)
        ans = 0
        for i in range(n):
            if nums[i]!=0:
                leftsum += nums[i]
                rightsum -= nums[i]
            else: 
                if leftsum == rightsum:
                    ans += 2
                elif abs(leftsum - rightsum) == 1:
                    ans += 1
        return ans


        # n = len(nums)
        # valid = 0
        # for i in range(n):
        #     if nums[i] != 0:
        #         continue 
        #     else:   
        #         for direction in (-1, 1): 
        #             #makr a copy of the array  because for each you are trying to edit it
        #             copyNums = nums[:]
        #             x = i
        #             while (0 <= x <= n-1):
        #                 if copyNums[x] == 0:
        #                     x += direction
        #                 else: 
        #                     copyNums[x] -= 1
        #                     direction *= -1
        #                     x += direction
        #             print(copyNums)

        #             # if it comes out of the loop with index out of bound, dont edit 'valid'
        #             if all(x==0 for x in copyNums):
        #                 valid += 1

        # return valid


    '''
    my understanding
    first find the zero element. they are the possible starting points
    iterate over each starting point
    have a left and right direction for each starting point
    if the pointer is still within 0 and n-1, then ... and inc count of valid
    if it goes out or if it doesnt become 0, then stop

    update: this has O(n^2)
    another code i saw in the solutions has managed to do it in O(n)
    counting the sum of left and right sub array taking 0 as center
    if lsum=rsum across any 0, then valid+=2
    if abs(lsum-rsum)=1, then valid+=1

    update 2: just now modified the code to have the second and faster approach
    it uses the prefix sum properly instead of simulating things
    if lsum==rsum, then it means from the zero, you can proceed in either directions and 
    since the sum is equal, the object/0 will bounce off and make both halves 0
    if abs(lsum-rsum)==1, then it means, you can start off only in one direction as proceeding 
    in the other will make it move out of the array

    '''