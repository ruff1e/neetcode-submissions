class Solution:
    def maxArea(self, heights: List[int]) -> int:
        

        # height = [1,7,2,5,4,7,3,6]

        n = len(heights)
        result = 0
        left, right = 0, n-1


        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            total = height * width
            result = max(result, total)

            if heights[left] < heights[right]:
                left += 1
            else: 
                right -= 1

        return result
