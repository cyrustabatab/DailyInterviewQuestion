



def sort_colors(a):


    low = mid = -1
    high = len(a)


    
    while mid + 1 < high:
        if a[mid + 1] == 0:
            a[low +1],a[mid + 1] = a[mid + 1],a[low + 1]
            low += 1
            mid += 1
        elif a[mid + 1] == 1:
            mid += 1
        else:
            a[mid +1],a[high -1] = a[high-1],a[mid + 1]
            high -= 1
    


if __name__ == "__main__":
    

    a = [0,1,2,2,1,1,2,2,0,0,0,0,2,1]

    print(a)

    sort_colors(a)

    print(a)
