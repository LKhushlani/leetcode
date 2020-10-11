class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:

    def reverseKgroupHelper(self, head, k, remainingNodes):

        if remainingNodes < k:
            return head
        
        count = 0
        prev,current = None, head
        while count < k and current is not None:
            count += 1 
            remainingNodes -=1
            next = current.next
            current.next = prev
            prev = current
            current = next
        if next:
            head.next =  self.reverseKgroupHelper(next,k, remainingNodes)

        return prev



    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        total_nodes = 0
        current = head
        while current is not None:
            total_nodes +=1 
            current = current.next
        return reverseKgroupHelper(head, k, total_nodes)




        