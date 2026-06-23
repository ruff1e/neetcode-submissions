class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        profit = 0
        n = len(prices)
        

        # prices = [10,1,5,6,7,1]

        for i in range(n):
            currProfit = 0
            right = i + 1
            while right < n:
                currProfit = prices[right] - prices[i]
                profit = max(profit, currProfit)
                right += 1
        return profit




