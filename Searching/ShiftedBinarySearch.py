# recursive, O logN time | P logn Space 
def shiftedBinarySearch(array, target):
    # Write your code here.
    return shiftedBinarySearchHelper(array , target, 0, len(array)-1)


def shiftedBinarySearchHelper(array, target, left, right):

    if left > right:
        return -1 

    middle = (left+ right ) // 2
    potentialMatch = array[middle]
    leftNum = array[left]
    rightNum = array[right]
    if potentialMatch == target:
        return middle
    elif leftNum < potentialMatch:
        if target < potentialMatch  and target >= leftNum:
            return shiftedBinarySearchHelper(array, target, left, middle-1)
        else:
            return shiftedBinarySearchHelper(array, target, middle+1, right)

    else:
        if target > potentialMatch  and target <= rightNum:
            return shiftedBinarySearchHelper(array, target, middle+1, right )
        else:
            return shiftedBinarySearchHelper(array, target, left, middle -1)


# ----------------------------------------------
# iterative 
def shiftedBinarySearch(array, target):
    # Write your code here.
    return shiftedBinarySearchHelper(array , target, 0, len(array)-1)


def shiftedBinarySearchHelper(array, target, left, right):

    while left <= right

        middle = (left+ right ) // 2
        potentialMatch = array[middle]
        leftNum = array[left]
        rightNum = array[right]
        if potentialMatch == target:
            return middle
        elif leftNum < potentialMatch:
            if target < potentialMatch  and target >= leftNum:
                right = middle-1
            else:
                left=middle+1

        else:
            if target > potentialMatch  and target <= rightNum:
                left = middle+1
            else:
                right = middle -1


    return -1

        


    

    
