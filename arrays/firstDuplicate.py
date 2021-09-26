def firstDuplicateValue(array):
    # Write your code here.
    for num in array:
        absVal = abs(num)
        if array[absVal-1]<0:
            return absVal
        array[absVal-1] *= -1

    return -1
        

print(firstDuplicateValue( [-2, -1, 5, 2, -3, 3, 4]))

