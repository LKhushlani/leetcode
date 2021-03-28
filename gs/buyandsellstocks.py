class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minPrice , maxProfit = float('inf'), 0
        if len(prices) == 0:
            return 0

        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif prices[i]-minPrice > maxProfit:
                maxProfit = prices[i]- minPrice

        return maxProfit
