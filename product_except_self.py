import unittest
import sys
import hashlib
import bisect
from collections import defautltdict



class Quack:

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []
        self.buffer = []

    def push(self,value):
        self.stack_1.append(value)


    def pop(self):
        if not self.stack_1 and not self.stack_2:
            raise ValueError("Empty Quack")


        if not self.stack_1:

            for _ in range(len(self.stack_2)//2):
                self.buffer.append(self.stack_2.pop())


            while self.stack_2:
                self.stack_1.append(self.stack_2.pop())


            while self.buffer:
                self.stack_2.append(self.buffer.pop())


        
        return self.stack_1.pop()

    
    def pull(self):
        if not self.stack_1 and not self.stack_2:
            raise ValueError("Empty Quack")

        if not self.stack_2:
            for _ in range(len(self.stack_1)//2):
                self.buffer.append(self.stack_1.pop())

            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())

            while self.buffer:
                self.stack_1.append(self.buffer.pop())


        return self.stack_2.pop()






class TimeMap:

    def __init__(self):
        self.times =[]
        self.values = []


    def get(self,time): 

        if not self.times:
            return
        
        index = bisect.bisect_left(self.times,time)

        if index < len(self.times) and self.times[index] == time:
            return self.values[index]
        elif index == len(self.times):
            return
        else:
            return self.values[index - 1]
    

    def set(self,time,value):

        index = bisect_left(self.times,time)

        if index < len(self.times) and self.times[index] == time:
            self.values[index] = value
        elif index == len(self.times):
            self.times.append(time)
            self.values.append(value)
        else:
            self.times.insert(index,time)
            self.values.insert(index,value)


class TimeDict:

    def __init__(self):
        self.map = defaultdict(TimeMap)

    def get(self,key,time):
        return self.map[key].get(time)

    def set(self,key,time,value):
        self.map[key].set(time,value)



class BloomFilter:

    def __init__(self,a=1000,k=3):
        self.a = [False] * a

        self.hash_algorithms = [hashlib.sha1,hashlib.md5,hashlib.shasha384,hashlib.sha512,hashlib.sha256]

        self.hash_functions = [self._get_hash_function(f) for f in self.hash_algorithms[:k]]


    def _get_hash_function(self,f):

        def hash_function(value):
            v = f(str(value).encode('utf-8')).hexdigest()
            return int(v,16) % len(self.a)
        
        return hash_function
    

    def add(self,key):

        for f in self.hash_functions:
            self.a[f(key)] = True


    def __contains__(self,key):
        return all(f(key) for f in self.hash_functions)




class BIT:

    def __init__(self,nums):
        self.a = [0] * (len(nums) + 1)


        for i,num in enumerate(nums):
            self.update(i + 1,num)

    def update(self,index,num):

        while index < len(self.a):
            self.a[index] += num
            index += index & -index


    def query(self,index):
        
        total = 0
        while index > 0:
            total += self.a[index]
            index -= index & -index

        return total

    def range_query(self,a,b):
        return self.query(b) - self.query(a - 1)



def divide(x,y):

    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")


    quotient = 0
    remainder = x
    power = 32
    y_power = y << 32


    while remainder >= y:
        while y_power > remainder:
            power -= 1
            y_power >>= 1


        quotient += 2**power 
        remainder -= y_power

    return quotient

def big_addition(x,y):

    assert x and y

    larger = len(max(x,y,key=len))

    s = [0] * (larger + 1)


    i,j = len(x) - 1,len(y) - 1
    carry = 0
    end = len(s) - 1
    while i >= 0 or j >= 0:
        value = (x[i] if i >= 0 else 0) + (y[j] if j >= 0 else 0) + carry
        carry = value // 10
        s[end] = value % 10
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







class InvalidSymbolException(Exception):

    def __init__(self,c):
        super().__init__(f"Invalid Symbol {c}")


def expression_evaluation(s):

    i = 0
    operand_stack = []
    operator_stack = []
    operators = {"*": 1,"/":1,"+": 0,"-":0}

    while i < len(s):
        c = s[i]
        if c == ' ':
            i += 1
            continue
        elif c.isdigit():
            j = i + 1
            number = [c]
            while j < len(s) and s[j].isdigit():
                number.append(s[j])
                j += 1

            operand_stack.append(int(''.join(number)))

            i = j
            continue
        elif c in operators:
            while operator_stack and operator_stack[-1] != '(' and operators[operator_stack[-1]] >= operators[c]:
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
    

    while operator_stack:
        evaluate(operator_stack,operand_stack)

    return operand_stack[0]
def evaluate(operator_stack,operand_stack):

    operations = {"*": lambda x,y: x * y,"/": lambda x,y: x/y, "+":lambda x,y: x + y,"-": lambda x,y: x -y}


    operand_2 = operand_stack.pop()
    operand_1 = operand_stack.pop()
    operator = operator_stack.pop()

    value = operators[operator](operand_1,operand_2)

    operand_stack.append(value)





def number_to_roman_numeral(numeral):
    mapping = {1000: 'M',500: 'D',100: 'C',50: 'L',10: 'X',5: 'V',1:'I',4: 'IV',9: 'IX',40: 'XL',90: 'XC',400: 'CD',900: 'CM'}
    numbers = [1000,900,500,400,100,90,50,40,9,5,4,1]
    numbers.reverse()
    
    result = []
    while numeral != 0:
        current_num = numbers.pop()
        if numeral >= current_num:
            quotient = min(3,numeral//current_num)
            result.extend([mapping[current_num]] * quotient)
            numeral -= quotient * current_num

    

    return ''.join(result)






def roman_numeral_to_number(numeral):
    
    mapping = {"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000}
    total = 0

    i = 0

    while i < len(numeral):
        if i + 1 < len(numeral) and mapping[numeral[i]] < mapping[numeral[i +1]]:
            total += mapping[numeral[i +1]] - mapping[numeral[i]]
            i += 2
        else:
            total += mapping[numeral[i]]
            i += 1

    
    return total

def rabin_karp(s1,s2):
    assert len(s1) >= len(s2)

    current_hash = target_hash = 0
    same = True
    x = 53
    
    for i in range(len(s2)):
        if same and s1[i] != s2[i]:
            same = False

        current_hash = current_hash * x + ord(s1[i])
        target_hash = target_hash * x + ord(s2[i])

    if same:
        return 0
    
    power = x**(len(s2) - 1)

    for i in range(len(s2),len(s1)):
        letter_to_remove,letter_to_add = s1[i - len(s2)],s1[i]
        current_hash = (current_hash - power * ord(letter_to_remove)) * x + ord(letter_to_add)
        if current_hash == target_hash and s1[i - len(s2) + 1:i + 1] == s2:
            return i - len(s2) + 1

    return -1






def product_except_self(a):
    
    products_before = []
    product = 1

    for num in a:
        products_before.append(product)
        product *= num


    products_after = []
    product = 1

    for num in reversed(a):
        products_after.append(product)
        product *= num

    result = []
    for i in range(len(a)):
        result.append(products_before[i] * products_after[len(a) - 1- i])
    
    return result

if __name__ == "__main__":
    
    roman_numeral = "DCXLVIII"

    print(roman_numeral_to_number(roman_numeral))
    

    class Test(unittest.TestCase):

        def setUp(self):
            self.sol = roman_numeral_to_number


        def test_case_1(self):
            roman_numeral = "DCXLVIII" 
            self.assertEqual(self.sol(roman_numeral),648)

        def test_case_2(self):
            roman_numeral = "MMMDCCXXIV"
            self.assertEqual(self.sol(roman_numeral),3724)

    

    #unittest.main(verbosity=2)


    #number = int(sys.argv[1])
    #print(number_to_roman_numeral(number))


    print(divide(25,7))





