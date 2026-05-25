class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            if prices[i] - minPrice > profit:
                profit = prices[i] - minPrice
        return profit
            


        