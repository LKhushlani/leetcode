# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSumsHelper(root, runningSum, sumList):
	if root is None:
		return []
	
	runningSum += root.value
	#print(runningSum)
	if root.left is not None:
		#print(runningSum)
		branchSumsHelper(root.left, runningSum,sumList)
	if root.right is not None:
		branchSumsHelper(root.right, runningSum, sumList)
	if root.right is None and root.left is None:
		#print("Sum List",sumList, running)
		sumList.append(runningSum)
		return sumList
		#print(sumList)
		#return 
	
	
def branchSums(root):
    # Write your code here.
	sums = []
	branchSumsHelper(root, 0, sums)
    return sums


