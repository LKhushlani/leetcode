from collections import Counter
# class Solution:
    # def minDominoRotations(self, A: List[int], B: List[int]) -> int:
def minDominoRotations(A, B):

    same , count_A, count_B = Counter(), Counter(A), Counter(B)
    print(same, count_A,count_B)
    sum = 0

    for a,b in zip(A,B):
        if a == b:
            same[a] +=1

    for i in range(1,7):
        if count_A[i] + count_B[i] - same[i] == len(A):
            return min(count_A[i], count_B[i]) - same[i]

    return -1












minDominoRotations([2,1,2,4,2,2], [5,2,6,2,3,2])





        
        
        
        
        
        
        