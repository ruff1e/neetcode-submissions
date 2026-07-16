class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        # nums = [3,4,5,6,1,2]
        #         l   m     r 

        n = len(nums)
        left, right = 0, n-1
        result = nums[0]

        while left <= right:
            if nums[left] < nums[right]:
                result = min(result, nums[left])
                break
            medium = (right+left) // 2
            result = min(result, nums[medium])
            if nums[medium] >= nums[left]:
                left = medium + 1
            else:
                right = medium - 1

        return result