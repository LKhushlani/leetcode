# [[10, 70, 20, 30, 50, 11, 30]] ,  Ans -> 110, [10, 20, 30, 50]
# On2 time , On space

def maxSumIncreasingSubsequence(array):

    maxSums = [num for num in array]

    for i in range(len(array)):
        for j in range(0, i):
            currentSum = array[i] + maxSums[j]
            if array[j] < array[i] and currentSum >= maxSum[i]:
                maxSum[i] = currentSum

