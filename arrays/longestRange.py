def largestRange(array):
    # Write your code here.
    bestRange = []
    numbers = {}
    maxLength = float("-inf")
    for n in array:
        numbers[n] = True

    for n in array:
        if numbers[n] == False:
            continue

        left  = n-1
        right = n+1 
        currentLength = 0
        while left in numbers:
            numbers[left] = False
            currentLength  += 1
            left -= 1

        while right in numbers:
            numbers[right] = False
            currentLength  += 1
            right += 1

        if currentLength > maxLength:
            maxLength = currentLength
            bestRange = [left +1, right-1]

    return bestRange

print(largestRange([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]))

        




