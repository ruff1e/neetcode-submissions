class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        

        # tasks = ["X","X","Y","Y"], n = 2
        # output = 5

        # X - Y - idle - X - Y      = 5


        # tasks = ["A","A","A","B","C"], n = 3
        # output = 9

        # A - B - C - idle - A - idle - idle - idle - A


        count = Counter(tasks)  # count = {A:3, B:1, C:1}
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)


        time = 0
        q = deque()  # pairs of [-cnt, idleTime]
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time