




def look_and_say_sequence(n):

    previous_term ="1"


    for _ in range(n -1):

        i = 0
        
        term = []
        while i < len(previous_term):
            c = previous_term[i]
            
            j = i
            count = 0
            while j < len(previous_term) and previous_term[j] == c:
                count += 1
                j += 1


            term.append(f"{count}{c}")

            i = j



        previous_term = ''.join(term)
    
    return previous_term


if __name__ == "__main__":

    
    for i in range(1,10):
        print(look_and_say_sequence(i))
    





        
        






