



def min_removals(s):


    open_count = 0
    invalid = 0


    for c in s:
        if c == '(':
            open_count += 1
        elif c == ')':
            if open_count > 0: 
                open_count -= 1
            else:
                invalid += 1



    return open_count + invalid
    


    






