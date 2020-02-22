




class MinMaxStack:


    def __init__(self):
        self.stack = []
        self.min_max_stack = []
        self.size = 0

    def __len__(self):
        return self.size
    

    def peek(self):
        if self.stack:
            return self.stack[-1]

        raise ValueError("Empty Stack")

    def min(self):
        if self.min_max_stack:
            return self.min_max_stack[-1]["min"]
        
        raise ValueError("Empty Stack")

    def max(self):
        if self.min_max_stack:
            return self.min_max_stack[-1]["max"]

        raise ValueError("Empty Stack")

    def enqueue(self,value):
        self.stack.append(value)
        
        self.size += 1

        min_max = {"min": value, "max": value}

        if self.min_max_stack:
            min_max = {"min": min(value,self.min_max_stack[-1]["min"]),"max": max(value,self.min_max_stack[-1]["max"])}

        self.min_max_stack.append(min_max)

    
    def dequeue(self):

        if self.stack:

            value = self.stack.pop()

            self.size -= 1

            self.min_max_stack.pop()

            return value


        raise ValueError("Empty Stack")







        








def rabin_karp(s1,s2):
    assert len(s1) >= len(s2)

    current_hash = target_hash = 0
    same = True
    x = 53

    for i in range(len(s2)):
        if same and s1[i] != s2[i]:
            same = True

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




def longest_common_substring(s1,s2):


    matrix = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

    
    longest = float('-inf')
    longest_index = None
    for i in range(1,len(matrix)):
        c1 = s1[i -1]
        for j in range(1,len(matrix[0])):
            c2 = s2[j -1]


            if c1 == c2:
                matrix[i][j] = 1 + matrix[i - 1][j - 1]
                if matrix[i][j] > longest:
                    longest = matrix[i][j]
                    longest_index = (i,j)




def longest_common_subsequence(s1,s2):


    matrix = [[[0,None] for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

    for i in range(1,len(matrix)):
        c1 = s1[i -1]
        for j in range(1,len(matrix[0])):
            c2 = s2[j -1]
        

            longest = float("-inf")
            case = None
            if c1 == c2:
                matrix[i][j][0] = matrix[i -1][j -1][0] + 1
                longest = matrix[i][j][0]
                case = 1

            case_2 = matrix[i][j -1][0]
            case_3 = matrix[i -1][j][0]

            maximum,max_case = max((longest,case),(case_2,2),(case_3,3),key=lambda x:x[0])
            matrix[i][j][0] = maximum
            matrix[i][j][1] = max_case

    

    subsequence = reconstruct_subsequence(matrix,s1,s2)
    print(subsequence)


def reconstruct_subsequence(matrix,s1,s2):
    i,j = len(matrix) - 1,len(matrix[0]) - 1
    
    subsequence  = []
    while i > 0 and j > 0:
        case = matrix[i][j][1]

        if case == 1:
            subsequence.append(s1[i -1])
            i -= 1
            j -= 1
        elif case == 2:
            j -= 1
        elif case == 3:
            i -= 1

    return ''.join(subsequence[::-1])



def longest_increasing_subsequence(a):

    longest = [[1,None] for _ in range(len(a))] 
    
    longest_number = 1
    longest_index = 0
    for i in range(1,len(a)):
        num_1 = a[i]
        for j in range(0,i):
            num_2 = a[j]
            if num_2 < num_1:
                longest[i][0],longest[i][1] = max((longest[i][0],longest[i][1]),(longest[j][0] + 1,j))
                if longest[i][0] > longest_number:
                    longest_number = longest[j][0]
                    longest_index = i


    
    longest_sequence = reconstruct_sequence(longest,longest_index,a)
    print(longest_sequence)







def reconstruct_sequence(longest,longest_index,a):


    i = longest_index

    sequence = []

    while i >= 0:
        sequence.append(a[i])

        i = longest[i][1]
        if i is None:
            break


    
    return sequence[::-1]

    

if __name__ == "__main__":
    
    a = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

    longest_increasing_subsequence(a)




