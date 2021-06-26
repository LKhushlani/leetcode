# Do not edit the class below except for
# the insert method. Feel free to add new
# properties and methods to the class.
#  Data Structure : Heaps 
# form 2 heaps 
# lower half (max heap)and greater Half(min heap)
# get max from lower half and min from greater half and calculate the median 
# keep track of numbers either insert in min and same way 
# insertion in heap is logn time than in array 
# if both have even lengths take 1 from both , even length
# else take top val of greatest length
# insertion in non empty heap  , add to end and sift up

class ContinuousMedianHandler:
    def __init__(self):
        # Write your code here.
        self.median = None
        self.lowers = Heap( MAX_HEAP_FUNC,[])
        self.highers = Heap(MIN_HEAP_FUNC,[])
	

    def insert(self, number):
        # Write your code here.
        if not self.lowers.length or self.lowers.peek() > number:
            self.lowers.insert(number)
        else:
            self.highers.insert(number)

        self.rebalanceHeaps()
        self.updateMedian()

    def rebalanceHeaps(self):
        if self.lowers.length - self.highers.length == 2:
            self.highers.insert(self.lowers.remove())
        elif self.highers.length - self.lowers.length == 2:
            self.lowers.insert(self.highers.remove())


    def updateMedian(self):
        if self.highers.length == self.lowers.length:
            self.median = (self.highers.peek() + self.lowers.peek()) / 2
        elif self.highers.length > self.lowers.length:
            self.median = self.highers.peek()
        else:
            self.median = self.lowers.peek()


    def getMedian(self):
        return self.median

	
	
# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class Heap:
    def __init__(self, comparisonFunc, array):
        # Do not edit the line below.
        self.comparisonFunc = comparisonFunc
        self.heap = self.buildHeap(array)
        self.length = len(self.heap)

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
            if childTwoIdx !=-1:
                if self.comparisonFunc(heap[childTwoIdx] , heap[childOneIdx]):
                    indexToSwap = childTwoIdx
                else:
                	indexToSwap = childOneIdx
			else:
				indexToSwap = childOneIdx
            if self.comparisonFunc(heap[indexToSwap] , heap[currentIdx]):
                self.swap(indexToSwap, currentIdx, heap)
                currentIdx = indexToSwap
                childOneIdx  = currentIdx *2 +1
            else:
                return


    def siftUp(self, currentIdx, heap):
        # Write your code here.
        # get Parent Value , compare vlue with parent , if less , swap and re calculate value of current idx , while loop
        # sifted all the way to top. need end conditino , if current > 0 
        parentIdx = (currentIdx - 1) // 2 
        while currentIdx > 0:
            if self.comparisonFunc( heap[parentIdx] , heap[currentIdx]):
                self.swap(parentIdx, currentIdx, self.heap)
                currentIdx = parentIdx
                parentIdx = (currentIdx - 1 ) // 2
            else:
                return
        
    def peek(self):
        # Write your code here.
        return self.heap[0]

    def remove(self):
        # Write your code here.
        #  swap top and last element, pop the last element, siftDown(top element)
        self.swap(0, self.length-1, self.heap)
        elementToRemove = self.heap.pop()
		self.length-=1
        self.siftDown(0,self.length-1, self.heap)
        return elementToRemove

    def insert(self, value):
        # Write your code here.
        self.heap.append(value)
		self.length += 1
        self.siftUp(self.length-1,self.heap)

    def swap(self, i , j, heap):
        heap[i], heap[j] =  heap[j], heap[i]


def MAX_HEAP_FUNC(a,b):
        return a>b

def MIN_HEAP_FUNC(a,b):
        return a<b


    
