'''
Given an array of roses. roses[i] means rose i will bloom on day roses[i]. Also given an int k, which is the minimum number of adjacent bloom roses required for a bouquet, and an int n, which is the number of bouquets we need. Return the earliest day that we can get n bouquets of roses.

Example:
Input: roses = [1, 2, 4, 9, 3, 4, 1], k = 2, n = 2
Output: 4
Explanation:
day 1: [b, n, n, n, n, n, b]
The first and the last rose bloom.

day 2: [b, b, n, n, n, n, b]
The second rose blooms. Here the first two bloom roses make a bouquet.

day 3: [b, b, n, n, b, n, b]

day 4: [b, b, b, n, b, b, b]
'''

def minDaysToBloom(roses, n, k):

    def noOfBouquetsOnThisDay(day):

        totalBoquets = 0
        adjBloomFlowers = []

        for flower in roses:
            if flower <= day:
                adjBloomFlowers.append('bloomed')

            else:
                totalBoquets += len(adjBloomFlowers)//k
                adjBloomFlowers = []
        
        totalBoquets += len(adjBloomFlowers)// k
        return totalBoquets


    totalFlowersNeeded = n*k
    totalFlowesWeGrow = len(roses)

    if totalFlowersNeeded > totalFlowesWeGrow:
        return -1
    
    min_day = 0
    max_day = max(roses)

    while min_day < max_day:
        current_day = min_day + (max_day-min_day) // 2

        if noOfBouquetsOnThisDay(current_day) < n:
            min_day = current_day+1
        
        else:
            max_day = current_day

    return min_day