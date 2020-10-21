# [2,3,1,-4,2]
def hasSingleCycle(array):
    # Write your code here.
    numberOfVisited = 0
    currentIdx = 0
	while numberOfVisited < len(array):
		
        if numberOfVisited>0 and currentIdx == 0:
            return False

        numberOfVisited += 1
        currentIdx = getnextIdxHelper(array, currentIdx)

    return currentIdx==0



def getnextIdxHelper(array, currentIdx):
    jump = array[currentIdx]
    nextIdx = (currentIdx+ jump) % len(array)
    return nextIdx if nextIdx>=0 else nextIdx + len(array)
    
