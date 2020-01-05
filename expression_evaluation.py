


def big_addition(x,y):

    assert x and y
    
    larger = max(x,y,key=len)

    result = [0] * (larger + 1)
    
    i,j = len(x) - 1,len(y) - 1
    carry = 0
    end = len(result) - 1
    
    while i >= 0 or j >= 0 or carry != 0:
        s = (x[i] if i >= 0 else 0) + (y[j] if j >= 0 else 0) + carry
        carry = s//10
        result[end] = s % 10
        i -= 1
        j -= 1
        end -= 1


    return result


def big_multiply(x,y):

    assert x and y

    x,y = (x,y) if len(x) >= len(y) else (y,x)
    
    result = None
    for i in reversed(range(len(y))):

        amount = (len(y) - 1 - i)
        subproduct = [0] * (amount + len(x) + 1)
        j = len(x) - 1
        carry = 0
        end = len(subproduct) -  1 - amount

        while j >= 0 or carry != 0:
            product = y[i] * (x[j] if j >= 0 else 0) + carry
            carry = product // 10
            subproduct[end] = product % 10
            j -= 1
            end -= 1

        result = subproduct if result is None else big_addition(result,subproduct)
    
    return result




class InvalidSymbolException(Exception):

    def __init__(self,c):
        super().__init__(f"Invalid character {c}")

def expression_evaluation(s):

    i = 0

    operand_stack = []
    operator_stack = []
    operators = {"*": 1,"/": 1,"+": 0,"-":0}
    
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
            operand_stack.append(number)
            i = j
            continue
        elif c in operators:
            while operator_stack and operator_stack[-1] != '(' and operators[c] <= operators[operator_stack[-1]]:
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

    operations = {"*": lambda x,y: x* y,"/":lambda x,y: x/y,"+": lambda x,y: x +y,"-": lambda x,y: x -y}


    n2 = operand_stack.pop()
    n1 = operand_stack.pop()
    operation = operator_stack.pop()

    value = operations[operation](n1,n2)

    operand_stack.append(value)


if __name__ == "__main__":
    
    s = "(3 * 4) + 3 / 2"
    print(s)
    print(expression_evaluation(s))


