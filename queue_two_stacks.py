



class QueueTwoStacks:

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []
    
    def enqueue(self,value):
        self.stack_1.append(value)

    def dequeue(self):

        if not self.stack_2:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())


        if not self.stack_2:
            raise ValueError("Empty Queue")

        return self.stack_2.pop()



