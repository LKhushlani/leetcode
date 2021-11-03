from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float("inf")
        maxProfit = -float('inf')
        for p in prices:
            
            minPrice = min(minPrice,p)
            maxProfit = max(maxProfit,p-minPrice)
            print(maxProfit)

        return maxProfit



stock = Solution()
res = stock.maxProfit([7,1,5,3,6,4])
print(res)

