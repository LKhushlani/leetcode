# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def binaryTreeDiameter(tree):
    # Write your code here
    return binaryTreeInfo(tree).diameter


def binaryTreeInfo(tree):

    if tree is None:
        return TreeInfo(0, 0)

    
    leftTreeInfo = binaryTreeInfo(tree.left)
    rightTreeInfo = binaryTreeInfo(tree.right)

    longestPathToRoot = leftTreeInfo.height + rightTreeInfo.height
    maxDiameterSoFar = max(leftTreeInfo.diameter, rightTreeInfo.diameter)
    currentDiameter   = max(maxDiameterSoFar, longestPathToRoot)
    currentHeight  = 1+ max(leftTreeInfo.height , rightTreeInfo.height)

    return TreeInfo(currentDiameter, currentHeight)



class TreeInfo:
    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height



