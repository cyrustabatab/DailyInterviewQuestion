



def move_zeros_to_end(a):

    mid = -1
    high = len(a)

    while mid + 1 < high:
        if a[mid + 1] == 0:
            a[mid + 1],a[high -1] = a[high -1],a[mid +1]
            high -= 1
        else: 
            mid += 1


if __name__ == "__main__":
    

    a = [0,0,0,2,0,1,3,4,0,0]

    print(a)

    move_zeros_to_end(a)

    print(a)
