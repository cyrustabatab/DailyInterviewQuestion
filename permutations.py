
def wis(a):

    maximum = [[float("-inf"),None] for _ in range(len(a) + 1)]

    maximum[0][0],maximum[0][1] = 0,2
    maximum[1][0] = a[0]
    maximum[1][1] = 2

    for i in range(2,len(a)):
        number = a[i -1]
        maximum[i][0] = max((number + maximum[i -2][0],2),(maximum[i-1][0],1),key=lambda x:x[0])
    
    sequence = reconstruct_wis(maximum,a)


def reconstruct_wis(maximum,a):

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








def min_coin_change(n,denoms):

    minimum = [[float("inf"),None] for _ in range(n + 1)]

    minimum[0][0] = 0

    for amount in range(1,len(minimum)):
        for i,denom in enumerate(denoms):
            if denom <= amount:
                minimum[amount][0],minimum[amount][1] =min((minimum[amount][0],minimum[amount][1]),(minimum[amount - denom][0] + 1,i),key=lambda x:x[0])


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
    



class BIT:

    def __init__(self,nums):
        self.a = [False] * (len(nums) + 1)

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



def combinations(a,k):
    aux_buffer = [None] * k
    a_index = 0
    buffer_index = 0
    combinations_helper(a,a_index,aux_buffer,buffer_index)

def combinations_helper(a,a_index,aux_buffer,buffer_index):

    if buffer_index == len(aux_buffer):
        print(aux_buffer)
        return


    for i in range(a_index,len(a)):
        aux_buffer[buffer_index] = a[i]

        combinations_helper(a,i + 1,aux_buffer,buffer_index + 1)
        aux_buffer[buffer_index] = None
    
def permutations(a,k):
    aux_buffer = [None] * k
    in_buffer = set()

    permutations_helper(a,aux_buffer,buffer_index,in_buffer)


def permutations_helper(a,aux_buffer,buffer_index,in_buffer):
    if buffer_index == len(aux_buffer):
        print(aux_buffer)
        return


    for i in range(len(a)):
        if i not in in_buffer:
            in_buffer.add(i)
            aux_buffer[buffer_index] = a[i]

            permutations_helper(a,aux_buffer,buffer_index + 1,in_buffer)

            aux_buffer[buffer_index] = None
            in_buffer.remove(i)

if __name__ == "__main__":
    

    denoms = [1,5,10,25]

    amount = 117

    print(min_coin_change(amount,denoms))
