class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        

        # nums = [1,2,2,3,3,3]     k = 2     output = [2,3]
        # edge cases: 
        # nums = [1]    k = 2
        # nums = [1,2,3,4,5]    k=3


        # hashmap = {1:1, 2:2, 3:3}

        mp = {}

        for num in nums:
            mp[num] = 1 + mp.get(num, 0)


        # key -> value
        # number -> occurence
        # mp = {1:1, 2:2, 3:3}

        arr = []

        for num, count in mp.items():
            arr.append([count, num])

        # arr = [[1:1], [2:2], [3:3]]
        
        arr.sort()

        # arr = [[1:1], [2:2], [3:3]]


        result = []

        while len(result) < k:
            result.append(arr.pop()[1])

        return result