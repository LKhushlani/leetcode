
# O(n^2) time and space
def maxSumIncreasingSubsequence(array):
    # Write your code here.
    # currnt_sum
    # max_sum = -float('inf')
    sequences = [None for _ in array]
    sumArray = [num for num in array]
    maxSumndex = 0
    for i in range(0,len(array)):
        for j in range(0,i):
            currentSum = array[i] + sumArray[j]
            if array[j] < array[i] and currentSum >= sumArray[i]:
                sumArray[i] = currentSum
                sequences[i] = j
            if sumArray[i] >= sumArray[maxSumndex]:
                maxSumndex = 1
    return [sumArray[maxSumndex], buildSequence(array, sequences, maxSumndex)]

def buildSequence(array, sequences, currentIndex):

    sequence = []
    while currentIndex is not None:
        sequence.append(array[currentIndex])
        currentIndex = sequences[currentIndex]

    return list(reversed(sequence))

maxSumIncreasingSubsequence([10, 70, 20, 30, 50, 11, 30])
# i = 2, 3
# j = 0, 1 , 2
# currS = 20+ 10
# sumArray = [10,80,30,40,0,0,0]


