


def find_h_index(publications):

    n = len(publications)
    buckets = [0] * (n + 1)


    for publication in publications:
        if publication < n:
            citations[publication] += 1
        else:
            citations[n] += 1


    total = 0
    i = n


    while i >= 0:
        total += citations[i]

        if total >= i:
            return i


        i -= 1


   
   return 0





