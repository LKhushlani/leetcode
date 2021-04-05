def maxPathSum(tree):
    # Write your code here.

    _ , maxPathSum = findMaxSum(tree)
    return maxPathSum
	
	
	
def findMaxSum(tree):

    if tree is None:
        return (0, float("-inf"))


    leftMaxSumAsBranch, leftMaxPathSum = findMaxSum(tree.left)
    rightMaxSumAsBranch, rightMaxPathSum = findMaxSum(tree.right)
    maxChildSumAsBranch = max(leftMaxSumAsBranch, rightMaxSumAsBranch)  # max of root + left , or root+ right 

    value = tree.value
    maxSumAsBranch = max(maxChildSumAsBranch + value, value)          # one side   
    maxSumAsRootNode  = max(leftMaxSumAsBranch + rightMaxSumAsBranch + value, maxSumAsBranch)   # triangle  
    maxPathSum = max(maxSumAsRootNode, leftMaxPathSum , rightMaxPathSum)     
    return (maxSumAsBranch, maxPathSum)




    



    
