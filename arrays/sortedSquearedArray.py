def sortedSquaredArray(array):
    # Write your code here.
    result = [0 for _ in array]
    start_idx = 0
    end_idx = len(array) -1

    for idx in reversed(range(len(array))):
        starting_num  = abs(array[start_idx])
        ending_num = abs(array[end_idx])

        if starting_num > ending_num:
            result[idx] = starting_num **2
            start_idx +=1
        else:
            result[idx] = ending_num ** 2
            end_idx -= 1
    return result
        
    
        
print(sortedSquaredArray([-10,-1,0,12]))