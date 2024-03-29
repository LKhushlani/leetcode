
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        oldCopy = {None: None}
        
        cur = head
        while cur is not None:
            copy = Node(cur.val)
            oldCopy[cur] = copy
            cur = cur.next
            
        cur = head
        while cur is not None:
            copy = oldCopy[cur]
            copy.next = oldCopy[cur.next]
            copy.random = oldCopy[cur.random]
            cur = cur.next
        
        return oldCopy[head]