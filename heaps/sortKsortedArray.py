O nlogK time , OK space 
def sortKSortedArray(array, k):
    # Write your code here.

    minHeapWithKElements = MinHeap(
							array[:min
								  (k+1, len(array))
								 ])
    nextIndexToInsert = 0
    for i in range(k+1, len(array)):
        minElement = minHeapWithKElements.remove()
        array[nextIndexToInsert] = minElement
        nextIndexToInsert += 1

        currentNum = array[i]
        minHeapWithKElements.insert(currentNum)
    
    while not minHeapWithKElements.isEmpty():
        minElement = minHeapWithKElements.remove()
        array[nextIndexToInsert]  = minElement
        nextIndexToInsert += 1


    return array


# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)
		
	def isEmpty(self):
		return len(self.heap) == 0

    # O n time , O1 space 
    def buildHeap(self, array):
        # Write your code here.
        firstParentIdx = (len(array) -2 )// 2
        for currentIdx in reversed(range(firstParentIdx+1)):
            self.siftDown(currentIdx, len(array)-1, array)

        return array
        
# o Log n 
    def siftDown(self, currentIdx, endIdx, heap):
        # Write your code here.
        # need to get both children, cal ch1= currentIdx *2  + 1 ch2 = currentIdx *2 +2 
        childOneIdx = (currentIdx* 2) +1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx *2 + 2 if currentIdx*2 +2 <= endIdx else -1
            if childTwoIdx !=-1 and heap[childTwoIdx] < heap[childOneIdx]:
                indexToSwap = childTwoIdx
            else:
                indexToSwap = childOneIdx
            if heap[indexToSwap] < heap[currentIdx]:
                self.swap(indexToSwap, currentIdx, heap)
                currentIdx = indexToSwap
                childOneIdx  = currentIdx *2 +1
            else:
                break


    def siftUp(self, currentIdx, heap):
        # Write your code here.
        # get Parent Value , compare vlue with parent , if less , swap and re calculate value of current idx , while loop
        # sifted all the way to top. need end conditino , if current > 0 
        parentIdx = (currentIdx - 1) // 2 
        while currentIdx > 0 and heap[parentIdx] > heap[currentIdx]:
            self.swap(parentIdx, currentIdx, self.heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1 ) // 2
        
    def peek(self):
        # Write your code here.
        return self.heap[0]

    def remove(self):
        # Write your code here.
        #  swap top and last element, pop the last element, siftDown(top element)
        self.swap(0, len(self.heap)-1, self.heap)
        elementToRemove = self.heap.pop()
        self.siftDown(0,len(self.heap)-1, self.heap)
        return elementToRemove

    def insert(self, value):
        # Write your code here.
        self.heap.append(value)
        self.siftUp(len(self.heap)-1,self.heap)

    def swap(self, i , j, heap):
        heap[i], heap[j] =  heap[j], heap[i]
