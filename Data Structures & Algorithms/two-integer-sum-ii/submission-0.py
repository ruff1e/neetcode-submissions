class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        

        # [1, 2, 3, 4, 5, 6]
        # target = 9
        # n = 6
        # left = 0
        # right = 6

        left, right = 0, len(numbers) - 1

        while left < right:
            curSum = numbers[left] + numbers[right]

            if curSum > target:
                right -= 1
            elif curSum < target:
                left += 1
            else:
                return [left + 1, right + 1]
        
        return []