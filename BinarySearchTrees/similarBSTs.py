# on2 time, On2 space 
def sameBsts(arrayOne, arrayTwo):
    # Write your code here.
    if len(arrayOne) != len(arrayTwo):
        return False

    if len(arrayOne) == 0 and len(arrayTwo) == 0:
        return True
	
	if arrayOne[0] != arrayTwo[0]:
        return False

    leftOne = getElementsSmaller(arrayOne)
    leftTwo = getElementsSmaller(arrayTwo)
    rightOne = getElementsGreaterAndEqualTo(arrayOne)
    rightTwo = getElementsGreaterAndEqualTo(arrayTwo)

    return sameBsts(leftOne, leftTwo) and sameBsts(rightOne, rightTwo)

def getElementsGreaterAndEqualTo(array):

    arr =[]
    for i in range(1, len(array)):
        if array[i] >= array[0]:
            arr.append(array[i])

    return arr

def getElementsSmaller(array):

    arr =[]
    for i in range(1, len(array)):
        if array[i] < array[0]:
            arr.append(array[i])

    return arr

    

        