from typing import List
class Solution:
    def coinChange(self, denoms: List[int], n: int) -> int:

        coins = [float('inf') for amt in range(0,n+1)]
        coins[0] = 1
        for denom in denoms:
            for amount in range(1,len(coins)):
                if amount <=denom:
                    print(amount,denom)
                    coins[amount] = min(coins[amount-denom], coins[amount]+1)
                    print(coins)

        return coins[-1] if coins[n]!= float('inf') else -1


print(Solution().coinChange( [1,2,5],11))


