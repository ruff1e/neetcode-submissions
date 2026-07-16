class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        # nums = [6,1,2,3,4,5]    target = 4
        #         l   m     r
        # index = -1 

        index = -1
        left, right = 0, len(nums)-1


        while left <= right:
            medium = (right + left) // 2
            if nums[medium] == target:
                index = medium
                break
            
            # check if we are on the left portion
            if nums[medium] >= nums[left]:
                if target < nums[left] or target > nums[medium]:
                    left = medium + 1
                else: 
                    right = medium - 1
            
            # means we are on the right portion
            else:
                if target < nums[medium] or target > nums[right]:
                    right = medium - 1
                else:
                    left = medium + 1

        return index