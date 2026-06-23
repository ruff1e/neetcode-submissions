class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        # s = "AAABABB"   k=1
        #       -----
        # longest=5    left=0   right=5

        count = {}
        longest = 0
        left = 0 
        maximumF = 0


        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            maximumF = max(maximumF, count[s[right]])

            while (right-left+1) - maximumF > k:
                count[s[left]] -= 1
                left += 1

            longest = max(longest, right-left+1)

        return longest
