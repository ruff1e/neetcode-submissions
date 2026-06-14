class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left, right = 0, 1
        profit = 0


        # [10, 1, 5, 6, 7, 1]
        
        while right < len(prices):
            if prices[left] < prices[right]:
                high = prices[right] - prices[left]
                profit = max(profit, high)
            else:
                left = right
            right += 1
        
        return profit