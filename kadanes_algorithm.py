



def kadanes(a):

    current_sum = 0
    max_sum = float("-inf")
    
    current_start = current_end = None
    max_start = max_end = None

    for i,num in enumerate(a):
        
        if num >= current_sum + num:
            current_sum = num
            current_start = current_end = i
        else:
            current_sum += num
            current_end += 1

        
        if current_sum > max_sum:
            max_sum = current_sum
            max_start,max_end = current_start,current_end
    
    return max_sum,a[max_start:max_end + 1]


if __name__ == "__main__":
    

    a = [34,-50,42,14,-5,86]

    print(kadanes(a))




