def nodeDepths(root):
    depthSum  = 0
    stack = [{'node': root, 'depth': 0}]
    while  len(stack) > 0:
        info = stack.pop()
        node, depth = info['node'], info['depth']
        if node is None:
            continue
        depthSum += depth
        stack.append({'node': node.left, 'depth': depth+1})
        stack.append({'node': node.right, 'depth': depth+1})
    return depthSum
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


root = {
  "nodes": [
    {"id": "1", "left": "2", "right": "3", "value": 1},
    {"id": "2", "left": "4", "right": "5", "value": 2},
    {"id": "3", "left": "6", "right": "7", "value": 3},
    {"id": "4", "left": "8", "right": "9", "value": 4},
    {"id": "5", "left": None, "right": None, "value": 5},
    {"id": "6", "left": None, "right": None, "value": 6},
    {"id": "7", "left": None, "right": None, "value": 7},
    {"id": "8", "left": None, "right": None, "value": 8},
    {"id": "9", "left": None, "right": None, "value": 9}
  ],
  "root": "1"
}
nodeDepths(root)
