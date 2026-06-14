class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        for num in range(len(nums)):
            for x in range(num+1, len(nums)):
                if nums[num] == nums[x]:
                    return True
        return False