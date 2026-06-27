class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-s for s in stones]

        heapq.heapify(stones)


        while len(stones) > 1:
            number1 = abs(heapq.heappop(stones)) #6
            number2 = abs(heapq.heappop(stones)) #4

            if number2 < number1:
                heapq.heappush(stones, (-1*(number1-number2)))

        stones.append(0)
        return abs(stones[0])