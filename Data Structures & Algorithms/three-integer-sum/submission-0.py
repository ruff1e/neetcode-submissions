class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        
        # nums = [-1,0,1,2,-1,-4]

        n = len(nums)
        nums.sort()
        answer = []
        
        # nums = [-4,-1,-1,0,1,2,3]
        #        [ i, left        right]




        for i in range(n):
            if nums[i] > 0:                         # if i is positive, we cant go back to 0 because the remanings are also positive
                break
            elif i > 0 and nums[i] == nums[i-1]:
                continue
            

            left, right = i+1, n-1
            
            while left<right:
                summ = nums[i] + nums[left] + nums[right]
                if summ == 0:
                    answer.append([nums[i], nums[left], nums[right]])
                    left, right = left+1, right-1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif summ < 0:
                    left += 1
                else: 
                    right -= 1
        
        return answer
                    
