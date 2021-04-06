#  [123]
# generate all permutations 
# 3! permutations 

def getPermutations(array):
    # Write your code here.

    permutations = []
    return getPermutationsHelper(array,0, permutations)


def getPermutationsHelper(array, i, permutations):

    if i == len(array)-1:
        permutations.append(array[:])

    for j in range(i, len(array)):
        swap(array, i, j)
        getPermutationsHelper(array ,i+1,permutations)
        swap(array, i ,j)

def swap(array,i ,j):
    array[i] , array[j] = array[j], array[i]

    

    
