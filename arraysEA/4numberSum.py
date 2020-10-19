# o n^2  time 
# o n^2 space 
def fourNumberSum(array, targetSum):
    # Write your code here.
    allpairsum = {}
    result = []
    for i in range(1, len(array)-1):
        for j in range(i+1, len(array)):
            currentSum = array[i]+ array[j]
            rem = targetSum - currentSum
            if rem in allpairsum:
                for pair in allpairsum[rem]:
                    result.append(pair+ [array[i], array[j]])

        for k in range(0,i):
            currentSum = array[i] + array[k]
            if currentSum not in allpairsum:
                allpairsum[currentSum] =  [[array[i], array[k]]]

            else:
                allpairsum[currentSum].append([array[k], array[i]])

    return result




                










                





