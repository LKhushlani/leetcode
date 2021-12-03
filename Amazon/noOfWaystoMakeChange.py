'''
n = 6
denoms = [1, 5]
denom = 1 

coins = [1,1,2,3,4,5,6]
index = [0,1,2,3,4,5,6]

denom = 5
 amt [denom] = min(coins[amt], coins[amt-denom] + 1 )

coins = [1,1,2,3,4,5,6]
index = [0,1,2,3,4,5,6]
'''

def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.

    coins = [0 for i in range(n+1)]
    coins[0] = 1 

    for denom in denoms:
        print(denom)
        for amt in range(1,n+1):
            if amt>=denom:
                coins[amt] += coins[amt-denom]
                print('amt',amt,coins[amt], coins[amt-denom], coins)

numberOfWaysToMakeChange(6,[1, 5])
                
                

