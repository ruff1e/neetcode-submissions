class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        # nums = [1,2,2,3,3,3], k = 2     output = [2,3]

        # hashmap {1:1, 2:2, 3:3}

        '''
            2
        3

        '''


        # count = {1:1, 2:2, 3:3}
        #        number:occurance
    
        count = {}
        
        for num in nums:
            count[num] = 1 + count.get(num, 0)



        # count = {1:7, 2:5, 3:6}

        heap = []


        for num in count.keys():
            heapq.heappush(heap, (count[num], num))

            if len(heap) > k:
                heapq.heappop(heap)


        '''
        [7,1]           [6,3]

        '''
    
        result = []

        for i in range(k):
            result.append(heapq.heappop(heap)[1])

        return result









