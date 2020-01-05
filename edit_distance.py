



def edit_distance(s1,s2):
    
    matrix = [[[j if i == 0 else i if j == 0 else 0,3 if i == 0 else 4 if j == 0 else 0] for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
    

    for i in range(1,len(matrix)):
        c1 = s1[i -1]
        for j in range(1,len(matrix[0])):
            c2 = s2[j - 1]

            minimum = float("inf")
            min_case = None
            if c1 == c2:
                minimum = matrix[i -1][j -1][0]
                min_case = 1
            
            case_2 = matrix[i -1][j -1][0] + 1 #change
            case_3 = matrix[i][j-1][0] + 1 #insertion
            case_4 = matrix[i - 1][j][0] +1 #deletion


            matrix[i][j][0],matrix[i][j][1] = min((minimum,min_case),(case_2,2),(case_3,3),(case_4,4),key=lambda x:x[0])


    
    return matrix[-1][-1][0]


if __name__ == "__main__":
    

    s1= "biting"
    s2 = "sitting"

    print(edit_distance(s1,s2))
