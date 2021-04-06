# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class TreeInfo:
    def __init__(self, isBalanced, height):
        self.isBalanced  = isBalanced
        self.height =height


def heightBalancedBinaryTree(tree):
    # Write your code here.
    treeInfo = getTreeInfo(tree)
    return treeInfo.isBalanced


def getTreeInfo(tree):

    if tree is None:
        return TreeInfo(True, -1)

    leftTreeInfo = getTreeInfo(tree.left)
    rightTreeInfo = getTreeInfo(tree.right)

    isBalanced = leftTreeInfo.isBalanced and rightTreeInfo.isBalanced and 
    (leftTreeInfo.height - rightTreeInfo.height) <=1 

    height = 1 + max(leftTreeInfo.height, rightTreeInfo.height)

    return TreeInfo(isBalanced, height)







