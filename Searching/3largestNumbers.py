def findThreeLargestNumbers(array):
    # Write your code here.
    result  = [None, None , None]
	for num in array:
        findThreeLargestNumbersHelper(result, num)

    return result

def findThreeLargestNumbersHelper(result, num):

    if result[2] is None or num > result[2]:
        shiftAndUpdate(result, num , 2) 

    elif result[1] is None or num > result[1]:
        shiftAndUpdate(result,num,  1) 

    elif result[0] is None or num > result[0]:
        shiftAndUpdate(result, num, 0)


def shiftAndUpdate(result, num, idx):

    for i in range(idx+1):
        if i == idx:
            result[i] = num
        else:
            result[i] = result[i+1] 
        