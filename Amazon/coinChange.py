from typing import List
class Solution:
    def coinChange(self, denoms: List[int], n: int) -> int:

        coins = [float('inf') for i in range(0,n+1)]
        coins[0] = 0
        for denom in denoms:
            print(denom)
            for amount in range(len(coins)):
                print(amount)
                if denom <= amount:
                    coins[amount] = min(coins[amount], coins[amount-denom]+1)
                    print(denoms)


        print(denoms[-1])



print(Solution().coinChange( [1,2,5],11))