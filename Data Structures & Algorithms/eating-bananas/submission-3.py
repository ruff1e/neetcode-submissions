class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        # piles = [1,4,3,2], h = 9
        # output = 2/h

        # [1h, 2h, 2h, 1h] = 6hours total, which is less than h=9, so it works


        # add everythin in the array 
        # piles = [1,4,3,2]   = 10
        # then check if that is under h given to us
        # if it is under, eating rate is 1
        # if not, increment rate by 1 and keep checking


        
        left, right = 1, max(piles)

        result = right

        while left <= right:
            medium = (left+right) // 2
            totalTime = 0

            for pile in piles:
                totalTime += math.ceil(pile / medium)
            
            if totalTime <= h:
                result = medium
                right = medium - 1
            else:
                left = medium + 1
            
        return result
