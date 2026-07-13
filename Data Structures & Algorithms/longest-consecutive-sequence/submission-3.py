class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        
        # nums = [2,20,4,10,3,4,5]
        # output = 4


        # hashset

        numSet = set(nums)
        longest = 0
        length = 0


        for num in nums:
            if num-1 not in numSet:
                length = 1
                while num+1 in numSet:
                    length += 1
                    num +=1

            longest = max(longest, length)

        return longest