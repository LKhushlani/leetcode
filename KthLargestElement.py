import heapq

def kthLargest(arr,k):
    heapmin = []
    
    if not k or k < 0 or arr is None:
        return None
    
    for num in arr:
        
        if len(heapmin) < k:
            heapq.heappush(heapmin, num)
            
        elif n > heapmin[0]:
            heapq.heappop(heapmin)
            heapq.heappus(heapmin,num)
            
    return minheap[0]
  
