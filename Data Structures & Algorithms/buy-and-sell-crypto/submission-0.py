class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max =0
        length = len(prices)

        for num in range(length):
            for i in range(num+1, length):
                profit = prices[i] - prices[num]
                if profit > max:
                    max = profit
            
        return max


