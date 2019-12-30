


def coin_change(n,denoms):

    minimum = [[float("inf"),None] for _ in range(n)]
    minimum[0][0] = 0
    for amount in range(1,n):
        for i,denom in enumerate(denoms):
            if denom <=amount:
                minimum[amount][0],minimum[amount][1] = min((minimum[amount - denom][0] + 1,i),(minimum[amount][0],minimum[amount][1]),key=lambda x:x[0])
    


    print(minimum)
    coins = reconstruct_coins(minimum,denoms)

    return coins

def reconstruct_coins(minimum,denoms):

    coins = {denom: 0 for denom in denoms}

    

    i = len(minimum) - 1

    while i > 0:

        case = minimum[i][1]

        if case is None:
            break
    

        coins[denoms[case]] += 1

        i -= denoms[case]
        
    return coins



def wis(a):
    maximum = [[float("-inf"),None] for _ in range(len(a) + 1)] 

    maximum[1][0],maximum[1][1] = a[0],2

    
    for i in range(2,len(maximum)):
        num = a[i -1]
        m,case = max((num + maximum[i-2][0],2),(maximum[i -1][0],1),key=lambda x:x[0])


        maximum[i][0],maximum[i][1] = m,case

    

    sequence = reconstruct_sequence(maximum,a)
    
    
    print(sequence)

def reconstruct_sequence(maximum,a):
    
    i = len(maximum) - 1
    sequence = []

    while i > 0:
        case = maximum[i][1]
        if case == 2:
            sequence.append(a[i -1])
            i -= 2
        else:
            i -= 1

    return sequence[::-1]


def knapsack(items,capacity):

    matrix = [[[0,None] for _ in range(capacity + 1)] for _ in range(len(items) + 1)]

    for i in range(1,len(matrix)):
        item_value,item_weight = items[i -1]
        for j in range(1,len(matrix[0])):
            if item_weight > j:
                matrix[i][j][0] = matrix[i -1][j][0]
                matrix[i][j][1] = 1
            else:
                case_1 = matrix[i -1][j][0]
                case_2 = matrix[i -1][j -item_weight][0] + item_value

                max_case,case = max((case_1,1),(case_2,2),key=lambda x:x[0])
                matrix[i][j][0],matrix[i][j][1] = max_case,case
    

    items_included = reconstruct_items(matrix,items)

def optimal_sequence_alignment(s1,s2,gap_penalty=1,mismatch_penalty=2):

    matrix = [[j if i == 0 else i if j == 0 else 0 for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]

    for i in range(1,len(matrix)):
        c1 = s1[i -1]
        for j in range(1,len(matrix[0])):
            c2 = s2[j -1]

            case_1 = matrix[i -1][j -1] + (mismatch_penalty if c1 != c2 else 0) 
            case_2 = matrix[i][j -1] + gap_penalty #gap in first string
            case_3 = matrix[i -1][j] + gap_penalty #gap in second string

            min_case = min(case_1,case_2,case_3)

            matrix[i][j] = min_case
    

    return matrix[-1][-1]




def reconstruct_items(matrix,items):

    i,j = len(matrix - 1),len(matrix[0]) - 1
    items_included = []
    while i > 0 and j > 0:
        case = matrix[i][j][1]
        if case == 2:
            items_included.append(items[i -1])
            j -= items[i -1][1]
            i -= 1
        else:
            i -= 1


    return items_included[::-1]



def compare(x,y):

    xy = int(str(x) + str(y))
    yx = int(str(y) + str(x))

    return 1 if xy < yx else -1


class MyCompare:

    def __init__(self,num):
        self.num =  num
    
    @staticmethod
    def compare(x,y):
        xy = int(str(x) + str(y))
        yx = int(str(y) + str(x))

        return 1 if xy < yx else -1

    def __lt__(self,other):
        return MyCompare.compare(self.num,other.num) ==-1

    



def largest_number_formed_from_array(a):

    print(sorted(a,key=MyCompare))


if __name__ == "__main__":


    a = [54,546,548,60]

    largest_number_formed_from_array(a)


    








