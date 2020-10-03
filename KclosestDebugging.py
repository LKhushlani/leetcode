from heapq import heappush, heappushpop
class Solution:
    def kClosest(self, points, K):
        
        closest = []
        for x,y in points:
            print(x,y)
            dist = -(x*x+ y *y)
            print(dist)
            if len(closest) < K:
                print("H",closest)
                heappush(closest,[x,y,dist])
                
            elif dist > closest[0][2]:
                print("J")
                print(closest)
                heappushpop(closest, [x,y, dist])
            
            print(closest[0][2])
                
        return [[x,y] for x,y,dist in closest]

points = [[3,3],[5,-1],[-2,4]]
K = 2
Solution().kClosest(points,K)

         
        