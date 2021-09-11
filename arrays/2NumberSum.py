def twoNumberSum(array, targetSum):
    # Write your code here'
    hashmap = {}
    for n in array:
        rem = targetSum - n
        if n not in hashmap:
            hashmap[rem] = True
        else:
            return [n,rem]

a = twoNumberSum([3, 7, -4, 8, 11, 1, -1, 6], 10)
print(a)

    
        

