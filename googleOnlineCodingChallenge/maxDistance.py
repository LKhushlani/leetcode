'''

The distance between 2 binary strings is the sum of their lengths after removing the common prefix. For example: the common prefix of 1011000 and 1011110 is 1011 so the distance is len("000") + len("110") = 3 + 3 = 6.

Given a list of binary strings, pick a pair that gives you maximum distance among all possible pair and return that distance.


                            Using 1011000 and 1011110
                                root
                                    F
                                  F
                                    F
                                      F
                                    F   F
                                  F       F
                                T       T
'''

# Move to left for 0 and right for 1
# marked flag indicates if a binary number ends on that node
class TreeNode:
    def __init__(self, marked = False):
        self.marked = marked
        self.left = None
        self.right = None
        
def find_max_distance(input_arr):
    
    def createTree(input_arr):
        root = TreeNode()
        for st in input_arr:
            node = root
            L = len(st)
            for i in range(L):
                if st[i] == '0':
                    if not node.left:
                        node.left = TreeNode()
                    node = node.left
                else:
                    if not node.right:
                        node.right = TreeNode()
                    node = node.right
            node.marked = True
        return root
    
    root = createTree(input_arr)
    
    # Returns a tuple a,b:
    # a - max_sum encountered in that subtree
    # b - height of the sub-tree
    def get_max_distance(node):
        if not node:
            return 0, 0
        
        left_max_sum, left_height = get_max_distance(node.left)
        right_max_sum, right_height = get_max_distance(node.right)
        
        max_sum = max(left_max_sum, right_max_sum)
        if node.marked or (node.left and node.right):
            max_sum = max(left_height + right_height, max_sum)
        
        current_height = max(left_height, right_height) + 1
        
        return max_sum, current_height
    
    return get_max_distance(root)[0]

input_arr = ["1011000", "1011110"]
print(find_max_distance(input_arr))
input_arr = ["111", "11"]
print(find_max_distance(input_arr))