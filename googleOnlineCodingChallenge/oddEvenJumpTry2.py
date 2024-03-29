from  typing import List

def oddEvenJumps( A):

    # sort indexes of A by values in A
    sorted_indexes = sorted(range(len(A)), key = lambda i: A[i])
    print(sorted_indexes)
    # generate list of indexes we can jump to next on odd jumps
    oddnext =   makeStack(sorted_indexes)
    print('oddnext',oddnext)

    # sort indexes of A by reverse order of their value in A
    sorted_indexes.sort(key = lambda i: A[i], reverse = True)
    print(sorted_indexes)
    # generate list of indexes we can jump to next on even jumps
    evennext =   makeStack(sorted_indexes)
    print('evennext', evennext)

    # initialize odd and even lists that will contain
    # the information of if the end can be reached
    # from the respective index
    odd = [False] * len(A)
    even = [False] * len(A)

    # the last index is always counted
    odd[len(A)-1] = even[len(A)-1] = True

    # iterate through A backwards, starting at next to last element
    for i in range(len(A)-2, -1, -1):

        # if an odd jump is available from current index,
        # check if an even jump landed on the index of the available
        # odd jump and set current index in odd to True if it did
        if oddnext[i] is not None:
            odd[i] = even[oddnext[i]]

        # if an even jump is available from current index,
        # check if an odd jump landed on the index of the available
        # even jump and set current index in even to True if it did
        if evennext[i] is not None:
            even[i] = odd[evennext[i]]

    # return the number of spots marked True in odd
    # we always start with an odd jump, so odd will
    # contain the number of valid jumps to reach the end
    return sum(odd)

# makes monotonic stack
def makeStack(   sorted_indexes):
    result = [None] * len(sorted_indexes)
    stack = []
    for i in sorted_indexes:
        while stack and i > stack[-1]:
            result[stack.pop()] = i
        stack.append(i)
    # delete stack as a memory optimization
    del stack
    return result


oddEvenJumps([5,1,3,4,2])


    