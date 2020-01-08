



    
def minimum_size_subarray(a,s):
    
    minimum_sum = 0
    minimum_length = float("inf")
    current_sum = a[0]
    left = right = 0
    longest_left = longest_right = None
    while right < len(a): 

        if current_sum >= s:
            if right - left + 1 < minimum_length:
                minimum_length = right - left  + 1
                longest_left,longest_right = left,right
            current_sum -= a[left]
            left += 1
        else: 
            right += 1

            try:
                current_sum += a[right]
            except IndexError:
                break

    

    return minimum_length,a[longest_left:longest_right + 1]



if __name__ == "__main__":
    
    
    a = [2,3,1,2,4,3]
    s =  7

    print(minimum_size_subarray(a,s))



