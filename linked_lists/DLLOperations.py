# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        # Write your code here.
        if self.head is None:
            self.head = node
            self.tail = node
            return 
        self.insertBefore(self.head, node)
        

    def setTail(self, node):
        # Write your code here.
        if self.tail is None:
            self.setHead(node)
            return 
        self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        # Write your code here.
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return 
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert
            
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert
        

    def insertAfter(self, node, nodeToInsert):
        # Write your code here.
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return 
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert                

    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        
        if position == 1: 
            self.setHead(nodeToInsert)
            return
        node = self.head
        currentPos = 1
        while node is not None and currentPos != position:
            node = node.next
            currentPos += 1
        if node is not None:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)
        

    def removeNodesWithValue(self, value):
        # Write your code here. 3
        node = self.head
        while node is not None:
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value  == value:
                self.remove(nodeToRemove)
   
    def remove(self, node):
        # Write your code here. 2. 
        # edge cases head tail 
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
            
        self.removeBindings(node)

    def containsNodeWithValue(self, value):
        # Write your code here. 1.
        current = self.head
        while current is not None and current.value != value:
            current = current.next
        return current is not None
    
    def removeBindings(self, node):
        if node.prev is not None:
            node.prev.next = node.prev
            
        if node.next is not None:
            node.next.prev = node.next
        
        node.next = None
        node.prev = None
            