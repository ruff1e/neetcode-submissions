class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        new = ""

        for c in s:
            if c.isalnum():
                new += c.lower().strip()

        reverse = new[::-1]

        if new == reverse:
            return True
        return False