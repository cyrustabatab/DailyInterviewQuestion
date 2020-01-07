


def eval(expression):

    return eval_helper(expression,0)[0]

def eval_helper(expression,index):
    

    result = 0
    operation = '+'
    while index < len(expression):
        c = expression[index]
        if c.isdigit():
            if operation == '+':
                result += int(c)
            else:
                result -= int(c)
        elif c in ('+','-'):
            operation = c
        elif c == '(':
            v,index = eval_helper(expression,index + 1)
            if operation ==  '+':
                result += int(v)
            else:
                result -= int(v)
        elif c == ')':
            return result,index

        index += 1



    return result,index    



    







def word_search(matrix,string):

    
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            c = matrix[row][col]
            if c == string[0]:

                #check down
                if row + len(string) <= len(matrix):
                    i = row + 1
                    for j in range(1,len(string)):
                        if i >= len(matrix) or matrix[i][col] != string[j]:
                            break
                        i += 1
                    else:
                        return True


                #check right
                if col + len(string) <= len(matrix[0]):
                    i = col + 1 
                    for j in range(1,len(string)):
                        if j >= len(matrix[0]) or matrix[row][i] != string[j]:
                            break
                        i += 1
                    else:
                        return True

    
    return False



if __name__ == "__main__":


    s = "-(4 + 3) - 5"

    print(eval(s))
    


