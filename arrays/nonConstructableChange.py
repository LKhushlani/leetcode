def nonConstructibleChange(coins):
    # Write your code here.
    coins.sort()

    currentChangeCreated = 0

    for coin in coins:
        if coin> currentChangeCreated+1:
            return currentChangeCreated+1

        currentChangeCreated += coin

    return currentChangeCreated+1


# Onlogn time 
# O1 space