
'''
n = 7
denoms = [1, 5, 10]
coins =  []
min coins = i need to make 7, 
1* 2 , 5 *1  = 3 coins 
[1,  float(inf),float(inf),float(inf),float(inf)]
[0     1 ]
'''
def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
    coins = [float('inf') for i in range(0,n+1)]
    coins[0] = 0
    for denom in denoms:
        print(denom)
        for amt in range(len(coins)):
            if amt >= denom:
                coins[amt] = min(coins[amt], coins[amt-denom] +1)
                print(coins)

    print(coins)


minNumberOfCoinsForChange(7,[1,5,10])


