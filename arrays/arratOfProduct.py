def arrayOfProducts(array):
    # Write your code here.
    result = [1 for _ in array]
    left_products = [1 for _ in array]
    right_products = [1 for _ in array]

    leftRunningProduct = 1 
    for i in range(len(array)):
        left_products[i] = leftRunningProduct
        leftRunningProduct *= array[i]

    rightRunningProduct = 1
    for i in reversed(range(len(array))):
        right_products[i] = rightRunningProduct
        rightRunningProduct *= array[i]

    for i in range(len(array)):
        result[i] = left_products[i] * right_products[i]


    return result


print(arrayOfProducts([5,1,4,2]))
     


