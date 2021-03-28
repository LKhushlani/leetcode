def indexEqualsValue(array):
    # Write your code here.

    return indexEqualsValueHelper(array, 0, len(array)-1)


def indexEqualsValueHelper(array, lefttIdx, rightIdx):

    if lefttIdx > rightIdx:
        return -1

    middleIdx = lefttIdx + (rightIdx - lefttIdx) // 2
    middleElement  = array[middleIdx]

    if middleElement < middleIdx:
        indexEqualsValueHelper(array, middleIdx+1, rightIdx)

    if middleElement == middleIdx and middleIdx == 0 :
        return middleIdx
    elif middleElement == middleIdx and array[middleIdx- 1] <middleIdx-1:
        return middleIdx
    else:
        return indexEqualsValueHelper(array, lefttIdx, middleIdx-1)




    
