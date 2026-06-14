class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # nums = [1,2,2,3,3,3]
        
        counts = {}

        for num in nums:
            counts[num] = 1 + counts.get(num, 0)


        # count = {1:1, 2:2, 3:3}
        # {number:appearance}

        arr = []

        for num, count in counts.items():
            arr.append([count, num])

        arr.sort()


        result = []

        while len(result) < k:
            result.append(arr.pop()[1])
        
        return result
