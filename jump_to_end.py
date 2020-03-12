



def min_jumps(a):


    minimum = [[float("inf"),None] for _ in range(len(a))]
    minimum[0][0] =0


    for i in range(1,len(minimum)):
        for j in range(i):
            amount = a[j]
            if amount + j >= i:
                minimum[i][0],minimum[i][1] = min((minimum[i][0],minimum[i][1]),(1 + minimum[j][0],j),key=lambda x:x[0])


    
    jumps = reconstruct_jumps(minimum,a) 

    print(jumps)


def reconstruct_jumps(minimum,a):
    

    sequence = []
    i = len(a) - 1
    current = i
    while current is not None:
        sequence.append(current)
        current = minimum[current][1]

    return sequence[::-1]



if __name__ == "__main__":
    
    a = [3,2,5,1,1,9,3,4]

    print(min_jumps(a))
