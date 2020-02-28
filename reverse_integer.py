



def reverse_integer(x):


    sign = [1,-1][x < 0]
    

    s = str(abs(x))

    reversed_s = s[::-1]
    result = int(reversed(s))
    

    if -(2**31) <= sign * result <= 2**31 -1:
        return  sign * result
    else:
        return 0









