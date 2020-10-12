class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    total_elements = 0
    current = head
    while current is not None:
        total_elements += 1
        current = current.next
    
    index = total_elements-k+1
    count = 1
    prevN, nextN = None, None
    node = head
    while count < index:
        prevN = node 
        node = node.next
        nextN = node
        count +=1 
    if count == index and index != 1:
        prevN.next = nextN.next

    if index == 1:
        head.value = head.next.value
        head.next = head.next.next



    
    
    


    






