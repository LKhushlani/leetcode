def threeNumberSum(array, targetSum):
    # Write your code here.
    
    result = []
    array.sort()
    for idx, num in enumerate(array):

        left_idx = idx+1
        right_idx = len(array)-1
        # current_sum = array[idx] + array[left_idx]+ array[right_idx]
        while left_idx < right_idx:
            current_sum = array[idx] + array[left_idx]+ array[right_idx]
            if current_sum > targetSum:
                right_idx -= 1
            elif current_sum < targetSum:
                left_idx += 1
            else:
                result.append([array[idx], array[left_idx], array[right_idx]])
                left_idx +=1
                right_idx -=1

    # return result

    print(result)

threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0)

        





