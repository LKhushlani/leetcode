# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
    # Write your code here.
	temp = current = LinkedList(-1)
	
	while headOne or headTwo:
        if headOne is not None and headTwo is not None:
            if headOne.value < headTwo.value:
                current.next = headOne
                headOne = headOne.next
                current = current.next
            else:
                current.next = headTwo
                headTwo = headTwo.next
                current = current.next

        elif headOne or headTwo:
            current.next = headOne if headOne else headTwo
            break

    return temp.next
        
        
