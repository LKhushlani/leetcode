'''
array: [5, 1, 22, 25, 6, -1, 8, 10]
seq : [1, 6, -1, 10]
'''
def isValidSubsequence(array, sequence):
    # Write your code here.

    seq_idx = 0
    count =0
    for i in range(len(array)):
        if seq_idx < len(sequence) and array[i] == sequence[seq_idx]:
            count +=1
            seq_idx += 1 
    return count == len(sequence)
    
print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10],[22, 25, 6]))