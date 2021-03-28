# Feel free to add new properties and methods to the class.
class MinMaxStack:
	def __init__(self, stack):
		self.stack = []
		self.MaxStack = []
 	
    def peek(self):
        # Write your code here.
        return self.stack[len(self.stack)-1]

    def pop(self):
        # Write your code here.
        if self.MaxStack.peek() == self.stack[len(self.stack)-1]:
            self.MaxStack.pop() 
		return self.stack.pop()

    def push(self, number):
        # Write your code here.
		newMax =  number
		if len(self.MaxStack):
			lastValue = self.MaxStack[len(self.MaxStack)-1]
			newMax = max(number, lastValue)
		self.MaxStack.append(newMax)
        self.stack.append(number)
		

    def getMax(self):
        # Write your code here.
        return self.MaxStack[len(self.MaxStack)-1]

	   


