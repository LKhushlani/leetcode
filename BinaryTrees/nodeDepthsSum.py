def nodeDepths(root):
    # Write your code here

    return nodeDepthsHelper(root, 0)


def nodeDepthsHelper(node, depth):

    if node is None:
        return 0
    return depth + nodeDepthsHelper(node.left, depth +1) + nodeDepthsHelper(node.right +1)  



# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
