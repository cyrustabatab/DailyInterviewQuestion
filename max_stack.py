

class MinMaxStack:

    def __init__(self):
        self.stack = []
        self.min_max_stack = []
    

    def max(self):
        if self.min_max_stack:
            return self.min_max_stack[-1]["max"]
        raise ValueError("Empty Stack")
    
    def min(self):
        if self.min_max_stack:
            return self.min_max_stack[-1]["min"]

        raise ValueError("Empty Stack")

    def push(self,value):
        self.stack.append(value)
        
        value = {"max": value,"min": value}
        if self.max_stack:
            value = {"max": max(value,self.max_stack[-1]),min(value,self.max_stack[-1])}

        self.max_stack.append(value)

    def pop(self):

        if self.stack:
            value = self.stack.pop()
            self.min_max_stack.pop()
            return value

        raise ValueError("Empty Stack")




class MaxStack:

    def __init__(self):
        self.stack = []
        self.max_stack = []
    
    def max(self):
        if self.max_stack:
            return self.max_stack[-1]

        raise ValueError("Empty Stack")


    def push(self,value):
        self.stack.append(value)

        if self.max_stack:
            self.max_stack.append(max(self.max_stack[-1],value))
        else:
            self.max_stack.append(value)

    
    def pop(self):

        if self.stack:
            value = self.stack.pop()
            self.max_stack.pop()

            return value

        raise ValueError("Empty Stack")



