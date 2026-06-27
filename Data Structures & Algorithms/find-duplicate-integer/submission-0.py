class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        

        # nums = [1,2,3,2,2]
        # output = 2


        numSet = set()

        for num in nums:
            if num in numSet:
                return num
            else:
                numSet.add(num)
