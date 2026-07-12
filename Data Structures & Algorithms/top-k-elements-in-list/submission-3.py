class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        mp = {}

        for num in nums:
            mp[num] = 1 + mp.get(num, 0)


        heap = []
        for num in mp.keys():
            heapq.heappush(heap, (mp[num], num))
            if len(heap) > k:
                heapq.heappop(heap)


        result = []

        for i in range(k):
            result.append(heapq.heappop(heap)[1])

        return result        