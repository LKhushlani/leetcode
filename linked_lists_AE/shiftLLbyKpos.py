# edge cases  k = 0, k > len(ll), k is -ve      then not from thr end but beginning 0-1-2-3-4-5-6-7
def shiftLinkedList(head, k):
    # Write your code here.
    total_elements = 0
	original_tail_node = head
	while node is not None:
		total_elements += 1
        original_tail_node = original_tail_node.next
        
    offset = abs(k) % total_elements
    if offset == 0:
        return head

    new_tail_pos = total_elements - offset if offset > 0 else offset

    new_tail_node = head
    for i in range(1, new_tail_pos):
        new_tail_node = new_tail_node.next

    original_tail_node.next = head
    newhead = new_tail_node.next
    new_tail_node.next = None
	return newhead


# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
