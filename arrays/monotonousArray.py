def isMonotonic(array):

    nonInc = True
    nonDec = True

    for i in range(1,len(array)):
        
        if array[i] < array[i-1]:
            nonDec = False
        if array[i] > array[i-1]:
            nonInc = False

    return nonDec or nonInc