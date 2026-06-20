class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        s1_count = {}
        for char in s1:
            s1_count[char] = 1 + s1_count.get(char, 0)
        
        window_count = {}
        for i in range(len(s2)):
            window_count[s2[i]] = 1 + window_count.get(s2[i], 0)
            
            if i >= len(s1):
                if window_count[s2[i - len(s1)]] == 1:
                    del window_count[s2[i - len(s1)]]
                else:
                    window_count[s2[i - len(s1)]] -= 1
            
            if window_count == s1_count:
                return True
        
        return False



        # s2 = "lecabee"
        # s1_count = {a:1, b:1, c:1}
        # window_count = {c:1, a:1, b:1, }
        # i = 4
        # len.s1 = 3