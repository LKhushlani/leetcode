# On time , O1 space 
def kadanesAlgoOrLargestSumSubArray(array):

    maxSum =  array[0]
    currentSum = array[0]
    for i in range(1,len(array)):
        num  = array[i]
        currentSum = max(num, currentSum+num)
        maxSum = max(currentSum, maxSum)

    print(maxSum)


kadanesAlgoOrLargestSumSubArray([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4])