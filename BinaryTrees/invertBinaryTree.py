def invertBinaryTree(tree):
    # Write your code here.

    if tree is None:
        return

    swapTree(tree)
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)   


def swapTree(tree):
    tree.left , tree.right = tree.right, tree.left


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None