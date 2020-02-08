class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []
        self.min_val = None

    def push(self, x: int):
        if self.arr == []:
            self.min_val = x
            print(self.min_val)
            self.arr.append(x)
        else:
            if x < self.min_val:
                self.min_val = x
                self.arr.append(x)
            else:
                self.arr.append(x)
        
    def pop(self):
        self.arr.pop()
        if len(self.arr) == 0:
            self.min_val = None
        else:
            self.min_val = min(self.arr)
         

    def top(self):
        return self.arr[len(self.arr)-1]
        
    def getMin(self):
        return self.min_val
