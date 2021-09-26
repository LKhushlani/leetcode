# o n^2  time 
# o n^2 space 
def fourNumberSum(array, targetSum):
    # Write your code here.
    pairSumDict = {}
    result = []

    for i in range(1,len(array)-1):
        for j in range(i+1,len(array)):
            currentSum = array[i] + array[j]
            rem = targetSum - currentSum
            if rem in  pairSumDict:
                for pair in pairSumDict[rem]:
                    print(pair)
                    result.append(pair + [array[i], array[j]])

        for k in range(0,i):
            pairSum = array[i] + array[k]
            if pairSum not in pairSumDict:
                pairSumDict[pairSum] = [[array[i], array[k]]]
            else:
                pairSumDict[pairSum].append([array[i], array[k]])

        print(pairSumDict)

    return result


print(fourNumberSum([7,6,4,-1,1,2], 16))
            




             




                










                





