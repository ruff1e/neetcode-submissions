class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        # [1,2,3,4,5,6] = start

        # [6,1,2,3,4,5] = 1
        # [5,6,1,2,3,4] = 2
        # [4,5,6,1,2,3] = 3
        # [3,4,5,6,1,2] = 4
        # [2,3,4,5,6,1] = 5
        # [1,2,3,4,5,6] = 6

        
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1