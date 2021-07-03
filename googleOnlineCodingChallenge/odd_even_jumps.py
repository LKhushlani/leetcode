'''
You are given an integer array arr. From some starting index, you can make a series of jumps. The (1st, 3rd, 5th, ...) jumps in the series are called odd-numbered jumps, and the (2nd, 4th, 6th, ...) jumps in the series are called even-numbered jumps. Note that the jumps are numbered, not the indices.

You may jump forward from index i to index j (with i < j) in the following way:

During odd-numbered jumps (i.e., jumps 1, 3, 5, ...), you jump to the index j such that arr[i] <= arr[j] and arr[j] is the smallest possible value. If there are multiple such indices j, you can only jump to the smallest such index j.
During even-numbered jumps (i.e., jumps 2, 4, 6, ...), you jump to the index j such that arr[i] >= arr[j] and arr[j] is the largest possible value. If there are multiple such indices j, you can only jump to the smallest such index j.
It may be the case that for some index i, there are no legal jumps.
A starting index is good if, starting from that index, you can reach the end of the array (index arr.length - 1) by jumping some number of times (possibly 0 or more than once).

Return the number of good starting indices.

 

Example 1:

Input: arr = [10,13,12,14,15]
Output: 2
Explanation: 
From starting index i = 0, we can make our 1st jump to i = 2 (since arr[2] is the smallest among arr[1], arr[2], arr[3], arr[4] that is greater or equal to arr[0]), then we cannot jump any more.
From starting index i = 1 and i = 2, we can make our 1st jump to i = 3, then we cannot jump any more.
From starting index i = 3, we can make our 1st jump to i = 4, so we have reached the end.
From starting index i = 4, we have reached the end already.
In total, there are 2 different starting indices i = 3 and i = 4, where we can reach the end with some number of
jumps.


'''
def oddEvenJumps( A):
    n = len(A)
    next_higher, next_lower = [0] * n, [0] * n

    stack = []
    for a, i in sorted([a, i] for i, a in enumerate(A)):
        print(a, i)

        while stack and stack[-1] < i:
            print("in")
            next_higher[stack.pop()] = i
        stack.append(i)
        print("out",stack)

    # stack = []
    # for a, i in sorted([-a, i] for i, a in enumerate(A)):
    #     while stack and stack[-1] < i:
    #         next_lower[stack.pop()] = i
    #     stack.append(i)

    # higher, lower = [0] * n, [0] * n
    # higher[-1] = lower[-1] = 1
    # for i in range(n - 1)[::-1]:
    #     higher[i] = lower[next_higher[i]]
    #     lower[i] = higher[next_lower[i]]
    # return sum(higher)

oddEvenJumps([5,1,3,4,2])


    