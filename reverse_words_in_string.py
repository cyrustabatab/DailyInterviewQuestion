



def reverse_words(s):

    s = list(s)




    i = 0

    while i < len(s):
        if s[i].isalpha():
            start = i
            j = i + 1
            while j < len(s) and s[j].isalpha():
                j += 1

            reverse(s,start,j -1)

            i = j
        else:
            i += 1
    
    return ''.join(s)
def reverse(a,low,high):


    while low < high:
        a[low],a[high] = a[high],a[low]
        low += 1
        high -= 1


if __name__ == "__main__":
    

    s = "The cat in the hat"

    print(reverse_words(s))
