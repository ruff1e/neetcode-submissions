class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        count = {}
        result = 0
        left = 0
        maximum = 0
        
        # right-left+1 = size of the window
        # {A:3, B:1}
        # maximum = 4
        # right = 5
        # left = 1

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            maximum = max(maximum, count[s[right]])

            while (right - left + 1) - maximum > k:
                count[s[left]] -= 1
                left += 1
            
            result = max(result, right-left+1)
        

        return result