'''
There are n guests who are invited to a party. The k-th guest will attend the party at time S[k] and leave the party at time E[k].

Given an integer array S and an integer array E, both of length n, return an integer denoting the minimum number of chairs you need such that everyone attending the party can sit down.

Example:

Input: S = [1, 2, 6, 5, 3], E = [5, 5, 7, 6, 8]
Output: 3
Explanation:

The 1st guest will arrive at time 1. We need one chair at time 1.
The 2nd guest will arrive at time 2. There are now two guests at the party, so we need two chairs at time 2.
The 5th guest will arrive at time 3. There are now three guests at the party, so we need three chairs at time 3.
The 4th guest will arrive at time 5 and, at the same moment, the 1st and 2nd guests will leave the party.
There are now two (the 4th and 5th) guests at the party, so we need two chairs at time 5.
The 3rd guest will arrive at time 6, and the 4th guest will leave the party at the same time.
There are now two (the 3rd and 5th) guests at the party, so we need two chairs at time 6. 
So we need at least 3 chairs.

'''
import heapq
def minNumberChairs(s, e):

    intervals = [[ s[i], e[i]] for i in range(len(s))]
    intervals.sort(key= lambda x:x[0])
    min_heap = []
    result = 0
    for interval in intervals:
        print(interval)
        if not min_heap or min_heap[0] > interval[0]:
            result +=1
            heapq.heappush(min_heap, interval[1])
            print(min_heap)

        else:
            heapq.heappop()
            heapq.heappush(min_heap, interval[1])
            print(min_heap)

    print(result)
    return result

minNumberChairs( [1, 2, 6, 5, 3], [5, 5, 7, 6, 8])




