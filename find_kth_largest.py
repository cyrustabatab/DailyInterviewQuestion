import random


def find_kth_largest(a,k):

    return _quickselect(a,len(a) - k) 

def _quickselect(a,k):

    low,high = 0,len(a) - 1

    while low <= high:

        p = partition(a,low,high)

        if p == k:
            return a[p]

        if k < p:
            high = p - 1
        else:
            low = p + 1

    
    return a[high]






def partition(a,low,high):

    pivot_index = random.randint(low,high)

    a[low],a[pivot_index] = a[pivot_index],a[low]

    pivot = a[low]

    i = low + 1
    j = i


    while j <= high:
        if a[j] < pivot:
            a[j],a[i] = a[i],a[j]
            i += 1
        j += 1


    a[low],a[i -1] = a[i -1],a[low]

    return i - 1


if __name__ == "__main__":
    
    a = [random.randint(1,500) for i in range(100)]

    print(a)
    print(sorted(a))
    k = 5
    print(find_kth_largest(a,k))

    


