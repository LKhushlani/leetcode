'''
time complexity : 
O MlogM + NlogN
O1 space 
'''

def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()
    idx_one = 0 
    idx_two = 0
    min_diffenence = float('inf') 
    while idx_one < len(arrayOne) and idx_two < len(arrayTwo):
        current_diffence = abs(arrayOne[idx_one] - arrayTwo[idx_two])

        if current_diffence < min_diffenence:
            min_diffenence  = min(current_diffence, min_diffenence)
            pair = [arrayOne[idx_one], arrayTwo[idx_two]]
        if arrayOne[idx_one] < arrayTwo[idx_two]:
            idx_one += 1
        else:
            idx_two += 1

    return pair

smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17])
    


