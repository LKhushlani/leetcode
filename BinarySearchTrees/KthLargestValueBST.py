# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeNode:
	def __init__(self, noOfVisitedNodes, latestVisitedNode):
		self.noOfVisitedNodes = noOfVisitedNodes
        self.latestVisitedNode = latestVisitedNode
	
def findKthLargestValueInBst(tree, k):
    # Write your code here.
    treeInfo = TreeNode(0, -1)
    reverseInorderTraversal(tree,treeInfo, k)
	return treeInfo.latestVisitedNode


# O(n+k) time , O h space  
def reverseInorderTraversal(node, treeInfo, k):

    if node is None or treeInfo.noOfVisitedNodes >=k:
        return 
    reverseInorderTraversal(node.right, treeInfo, k)
    if treeInfo.noOfVisitedNodes < k:
        treeInfo.noOfVisitedNodes += 1
        treeInfo.latestVisitedNode  = node.value
        reverseInorderTraversal(node.left,treeInfo, k)

    