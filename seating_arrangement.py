
''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

import heapq
def main():
 # Write code here
    N, P  = input().split()
    N  = int(N)
    P = int(P)

    array = [0] * N
    heap = []

    for i in range(1, P+1):
        # print("I", i)
        if i == P:
            print(allotSeat(array, heap)+1)

        allotSeat(array, heap)

def allotSeat(array, heap):
    if array[0] == 0:
        array[0] = 1
        return 0
    if array[len(array)-1] == 0:
        distance = -(len(array)-2)
        # print("when p = 2", distance)
        heapq.heappush(heap, [distance, 0, len(array)-1])
        array[len(array)-1] = 1
        return len(array)-1

    currentSeat = heapq.heappop(heap)
    distance, start , end = currentSeat
    print(currentSeat)
    mid = (start + end ) // 2
    d1 = -(mid-start)
    d2 = -(end - mid)
    print("mid, d1, d2", mid, d1, d2)
    heapq.heappush(heap, [d1, start, mid])
    heapq.heappush(heap, [d2, mid, end])
    heapq.heapify(heap)
    print(heap)
    return mid

main()

