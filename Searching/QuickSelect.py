# like quick sort  
# 
def quickselect(array, k):
    # Write your code here.
    position  = k-1
    return quickSelectHelper(array, 0, len(array)-1, position)

def quickSelectHelper(array, startIdx, endIdx, position):

    while True:
        if startIdx > endIdx:
            raise Exception("Something wrong here")
        
        pivot = startIdx 
        left = startIdx +1 
        right = endIdx
        while left <= right:
            if array[left] > array[pivot] and array[right] < array[pivot]:
                swap(left, right, array)
            if array[left] < array[pivot]:
                left +=1
            if array[right] > array[pivot]:
                right -=1
        swap(pivot, right, array)
        if right == position:
            return array[right]
        elif right < position:
            startIdx  = right +1 
        else:
            endIdx = right -1 

def swap(one, two, array):
    array[one], array[two]  = array[two], array[one]
      







