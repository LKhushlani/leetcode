# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Collection

import collections
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:

        max_sum , level, max_level = -float('inf'), 0, 0
        q = collections.deque()
        q.append(root)

        while q:
            level  +=1
            level_sum = 0
            
            for _ in range(len(q)):    
                node  = q.popleft()  
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                max_level  = level

        return max_level

            
                




        


        