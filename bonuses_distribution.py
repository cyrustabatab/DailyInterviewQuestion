




def distribute_bonuses(performances):

    bonuses = [1] * len(performances)


    for i,performance in enumerate(performances):
        if (i > 0 and performance > performances[i -1]) and (i < len(performances) - 1 and performance > performances[i + 1]):
            bonuses[i] = 3
        elif (i > 0 and performance > performances[i -1]) or ( i < len(performances) - 1 and performance > performances[i + 1]):
            bonuses[i] = 2
    

    return bonuses

        

if __name__ == "__main__":
    

    p = [1,2,3,2,3,5,1]

    print(distribute_bonuses(p))


