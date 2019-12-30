




def dnf(a):

    low = mid = -1
    high = len(a)


    while mid + 1 < high:
        if a[mid + 1] == 1:
            a[low +1],a[mid + 1] = a[mid + 1],a[low + 1]
            mid += 1
            low += 1
        elif a[mid + 1] == 2:
            mid += 1
        else:
            a[high -1],a[mid + 1] = a[mid + 1],a[high -1]
            high -= 1



if __name__ == "__main__":
    

    a = [1,2,3,3,1,2,2,1]

    print(a)

    dnf(a)

    print(a)
