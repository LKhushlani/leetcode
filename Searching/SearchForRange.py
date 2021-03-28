#  [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73]
# 45 
# [starting , ending_index]
#  recursive
def searchForRange(array, target):
    # Write your code here.
    finalRange = [-1, -1]
    searchForRangeHelper(array, target, 0, len(array)-1, finalRange,True)
    searchForRangeHelper(array, target, 0, len(array)-1, finalRange,False)
    return finalRange


def searchForRangeHelper(array, target, start, end, finalRange, goLeft):

    if start > end:
        return
    middle = (start + end) // 2 
    if target > array[middle]:
        searchForRangeHelper(array, target, middle+1, end, finalRange, goLeft)

    elif target < array[middle]:
        searchForRangeHelper(array, target, start, middle-1, finalRange, goLeft)
    else:
        if goLeft:
            if middle == 0 or target != array[middle-1]:
                finalRange[0] = middle
            else:
                searchForRangeHelper(array, target, start, middle-1, finalRange, goLeft)
        else:
            if middle == len(array)-1 or target != array[middle+1]:
                finalRange[1] = middle
            else:
                searchForRangeHelper(array, target, middle+1, end, finalRange , goLeft)


#  iterative 
def searchForRange(array, target):
    # Write your code here.
    finalRange = [-1, -1]
    searchForRangeHelper(array, target, 0, len(array)-1, finalRange,True)
    searchForRangeHelper(array, target, 0, len(array)-1, finalRange,False)
    return finalRange


def searchForRangeHelper(array, target, start, end, finalRange, goLeft):

    while start <= end:
        middle = (start + end) // 2 
        if target > array[middle]:
            start = middle +1 

        elif target < array[middle]:
            end = middle -1 
        else:
            if goLeft:
                if middle == 0 or target != array[middle-1]:
                    finalRange[0] = middle
                    return 
                else:
                    end =  middle-1
            else:
                if middle == len(array)-1 or target != array[middle+1]:
                    finalRange[1] = middle
                    return
                else:
                    start = middle +1 

