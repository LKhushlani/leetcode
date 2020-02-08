# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = curr = ListNode(-1)
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                    curr = curr.next
                else:
                    curr.next = l2
                    l2 = l2.next
                    curr = curr.next
            elif l1 or l2:
                curr.next = l1 if l1 else l2
                break 
        return dummy.next
