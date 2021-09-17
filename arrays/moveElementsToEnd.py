def moveElementToEnd(array, toMove):
    # Write your code here.
    start_idx = 0 
    end_idx = len(array)-1

    while start_idx <= end_idx:
        
        while array[end_idx] == toMove:
            end_idx -= 1

        if array[start_idx] == toMove:
            array[start_idx] , array[end_idx] = array[end_idx], array[start_idx]

        return array


moveElementToEnd([2,1,2,2,2,3,4,2], 2)
        

    



