


def big_addition(x,y):
    assert x and y


    larger = len(max(x,y,key=len))

    s = [0] * (larger + 1)

    i,j = len(x) - 1,len(y) - 1
    carry = 0
    end = len(s) - 1
    while i >= 0 or j >= 0 or carry != 0:
        result = (x[i] if i >= 0 else 0) + (y[j] if j >= 0 else 0) + carry
        carry = carry // 10
        s[end] = carry % 10

        end -= 1
        i -= 1
        j -= 1

    return result

def big_multiply(x,y):
    
    assert x and y

    x,y = (x,y) if len(x) >= len(y) else (y,x)

    result = None


    for i in reversed(range(len(y))):
        amount = (len(y) - 1 - i)

        subproduct = [0]  * (amount + 1 + len(x))
        
        j = len(x) - 1
        carry = 0 
        end = len(subproduct) - 1- amount

        while j >= 0 or carry != 0:
            product=  y[i] * (x[j] if j >= 0 else 0) + carry
            carry = product // 10
            subproduct[end] = product % 10
            end -= 1
            j -= 1


        result = subproduct if result is None else big_addition(result,subproduct)

    
    return result





class MaxQueue:

    def __init__(self):
        self.size = 0
        self.queue = deque()
        self.max_queue = deque()

    def __len__(self):
        return self.size

    def enqueue(self,value):
        self.queue.append(value)

        while self.max_queue and value > self.max_queue[-1]:
            self.max_queue.pop()

        self.max_queue.append(value)


    def dequeue(self):
        if self.queue:
            if self.queue[0] == self.max_queue[0]:
                self.max_queue.popleft()

            return self.queue.popleft()
        

        raise ValueError("Empty Queue")
                


class MinMaxStack:

    def __init__(self):
        self.stack = []
        self.min_max_stack = []
        self.size = 0
    
    @property
    def empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def min(self):
        if self.min_max_stack:
            return self.min_max_stack[-1]["min"]
    
    def max(self):
        if self.min_max_stack:
            return self.min_max_stack[-1]["max"]

    def push(self,value):
        self.stack.append(value)
        value = {"min": value,"max": value}

        if self.min_max_stack:
            value = {"min": min(value,self.min_max_stack[-1]["min"]),"max": max(value,self.min_max_stack[-1]["max"])}
            self.min_max_stack.append(value)


        self.min_max_stack.append(value)
    

    def pop(self):
        if self.stack:
            value = self.stack.pop()

            self.min_max_stack.pop()


            return value

        
        raise ValueError("Empty Stack")
                        






class Node:

    def __init__(self,value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Node({self.value})"


def display(ll):

    current = ll

    while current:
        print(current.value,end=('->' if current.next else '\n'))
        current = current.next




def add_two_ll(l1,l2):


    current_1,current_2 = l1,l2
    
    
    head = None
    current = None
    carry = 0
    while current_1 or current_2 or carry != 0:
        s = (current_1.value if current_1 else 0) + (current_2.value if current_2 else 0) + carry
        carry = s // 10
        result = s % 10
        if not current:
            current = Node(result)
            head = current
        else:
            current.next = Node(result)
            current = current.next

        if current_1:
            current_1 = current_1.next

        if current_2:
            current_2 = current_2.next


    

    return head


class InvalidSymbolException(Exception):

    def __init__(self,c):
        super().__init__(f"Invalid Symbol {c}")

def expression_evaluation(s):

    i = 0
    operand_stack = []
    operator_stack = []
    operators = {"*": 1,"/": 1,"+": 0,"-": 0}

    while i < len(s):
        c = s[i]
        if c == ' ':
            i += 1
            continue
        elif c.isdigit():

            j = i
            number = []

            while j < len(s) and s[j].isdigit():
                number.append(s[j])
                j += 1

            number = int(''.join(number))
            i = j
            operand_stack.append(number)
            continue
        elif c in operators:
            while operator_stack and operator_stack[-1] != '(' and operators[c] <= operator_stack[operator_stack[-1]]:
                evaluate(operator_stack,operand_stack)

            operator_stack.append(c)
        elif c == '(':
            operator_stack.append(c)
        elif c == ')':
            while operator_stack and operator_stack[-1] != '(':
                evaluate(operator_stack,operand_stack)

            operator_stack.pop()
        else:
            raise InvalidSymbolException(c)

        i += 1
    

    while operator_stack:
        evaluate(operator_stack,operand_stack)


    return operand_stack[0]



def evaluate(operator_stack,operand_stack):
    
    operations = {"*": lambda x,y: x *y,"/": lambda x,y: x /y, "+": lambda x,y: x +y,"-": lambda x,y: x-y}
    n2 = operand_stack.pop()
    n1 = operand_stack.pop()
    
    operation = operator_stack.pop()

    value = operations[operation](n1,n2)

    operand_stack.append(value)








    




if __name__ == "__main__":
    
    

    n1 = Node(2)
    n2 = Node(4)
    n3 = Node(3)

    n4 = Node(9)
    n5 = Node(6)
    n6 = Node(9)

    n1.next = n2
    n2.next = n3

    n4.next = n5
    n5.next =n6


    display(n1)

    display(n4)

    result= add_two_ll(n1,n4)

    display(result)

