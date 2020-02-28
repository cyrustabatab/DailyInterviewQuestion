



# a = [1,2,3,4,5]

#a = [4,5,1,2,3]



def is_valid(a,capacity,d):


    current_sum = 0
    count = 0
    for weight in a:
        current_sum += weight

        if current_sum > capacity:
            current_sum = 0
            count += 1
            if count > d:
                return False


    return True





#O(nlog(sum(n)))
def split_array_largest_sum(a,days):

    min_capacity = max(a)
    max_capacity = sum(a)

    
    result = float("inf")
    while min_capacity < max_capacity:
        capacity = (min_capacity + max_capacity) // 2

        count = get_count(a,capacity)
        
        if is_valid(a,capacity,days):
            result = capacity

            max_capacity = capacity - 1
        else:
            min_capacity = capacity + 1


    return result













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
def shifted_binary_search(a):

    low,high = 0,len(a) - 1
    pivot = a[-1]



    while low < high:

        mid = (low + high) // 2

        if a[mid] <= pivot and ((mid == 0 or a[mid -1] > a[mid]) and (mid == len(a) - 1 or a[mid + 1] > a[mid])):
            return a[mid]
        elif a[mid] < pivot:
            high = mid - 1
        else:
            low = mid + 1





def min_range_needed_to_sort(a):


    maximum_so_far = float("-inf")
    max_index = None
    for i in range(len(a)):
        num = a[i]
        if num < maximum_so_far:
            max_index =i


        maximum_so_far = max(maximum_so_far,num)


    minimum_so_far = float("inf")
    min_index = None

    for i in range(len(a) - 1,-1,-1):
        num = a[i]

        if num > minimum_so_far:
            min_index = i

        minimum_so_far= min(minimum_so_far,num)


    return (min_index,max_index)



if __name__ == "__main__":
    

    a = [5,2,3,4,5]

    print(min_range_needed_to_sort(a))


