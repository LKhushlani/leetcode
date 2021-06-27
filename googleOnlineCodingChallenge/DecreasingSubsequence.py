'''
Given an int array nums of length n. Split it into strictly decreasing subsequences. Output the min number of subsequences you can get by splitting.

Example 1:

Input: [5, 2, 4, 3, 1, 6]
Output: 3
Explanation:
You can split this array into: [5, 2, 1], [4, 3], [6]. And there are 3 subsequences you get.
Or you can split it into [5, 4, 3], [2, 1], [6]. Also 3 subsequences.
But [5, 4, 3, 2, 1], [6] is not legal because [5, 4, 3, 2, 1] is not a subsuquence of the original array.

'''
from bisect import bisect
def decreasingSubsequence(arr):

    sequences = []
    tails = []

    for n in arr:
        pos = bisect(tails, n)

        if pos == len(tails):
            tails.append(n)
            sequences.append([])

        else:
            sequences[pos].append(tails[pos])
            tails[pos] = n 

    for i,tail in enumerate(tails):
        sequences[i].append(tail)

    return sequences

print(decreasingSubsequence([5, 2, 4, 3, 1, 6]))
