import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        # if matrix is Empty:
        #     return None
        # else:
        res = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if len(res) <k:
                    heapq.heappush(res,-(matrix[i][j])) 
                else:
                    heapq.heappushpop(res, -matrix[i][j])
        return -(res[0])
