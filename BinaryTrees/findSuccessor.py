# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

'''
2 condtions for Oh solution 
         1
        /  '\'
       2    3
    /  \    
   4    5

for node 2 , ans 5
if node has right child then get the left most child in right tree 

Condition 2: 
if no right child then continum to find the right most parent of the node 
eg find successor of node 5  
 5 parent 2,  3 parent 1 
'''


def findSuccessor(tree, node):

    if node.right is not None:
        return getLeftmostChild(node.right)

    return getRightmostParent(node)

def getLeftmostChild(node):
    currentNode = node
    while currentNode.left is not None:
        currentNode  = currentNode.left
    return currentNode

def getRightmostParent(node):
    currentNode  = node
    while currentNode.parent is not None and currentNode.parent.right  == currentNode:
        currentNode = currentNode.parent

    return currentNode.parent



