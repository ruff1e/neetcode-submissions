class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        profit = 0
        left, right = 0, 1
        

        # prices = [10,1,5,6,7,1]

        while right < len(prices):
            if prices[left] < prices[right]:
                currProfit = prices[right] - prices[left]
                profit = max(profit, currProfit)
            else:
                left = right
            right += 1

        return profit




