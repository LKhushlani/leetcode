def maxSumNonAdjacent(array):


    maxSum = array[:]
    # print(maxSum)
    maxSum[1] = max( maxSum[0], maxSum[1])

    for i in range(2, len(array)):
        maxSum[i] = max(maxSum[i-1], maxSum[i]+maxSum[i-2])
        print(maxSum[i-1], maxSum[i]+maxSum[i-2])
        # print(i, maxSum)


    return maxSum[-1]


print(maxSumNonAdjacent([75, 105, 120, 75, 90, 135]))