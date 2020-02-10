from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if nums is [] or k is None:
            return []
        else:
            result = []
                        
            count = {}
            
            for i in nums:
                if i in count:
                    count[i]+=1
                else:
                    count[i]=1
            
            for key,val in count.items():
                if len(result)<k:
                    heapq.heappush(result, (val,key))
                else:
                    heapq.heappushpop(result, (val,key))

            return [j for i,j in result]
