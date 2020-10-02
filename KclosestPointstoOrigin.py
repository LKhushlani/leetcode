from heapq import heappush, heappushpop
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        closest = []
        for x,y in points:
            dist = -(x*x+ y *y)
            if len(closest) < K:
                heappush(closest,[dist,x,y])
                
            elif dist > closest[0][0]:
                heappushpop(closest, [dist,x,y])
            
            print(closest)
                
                
        return [[x,y] for dist,x,y in closest]
            
            
            
        

            

            
            
        
         
        