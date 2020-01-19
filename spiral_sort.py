
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

    if same:
        return 0

    power = x**(len(s2) - 1)

    for i in range(len(s2),len(s1)):
        letter_to_remove,letter_to_add = s1[i - len(s2)],s1[i]
        current_hash = (current_hash - power * ord(letter_to_remove)) * x + ord(letter_to_add)
        if current_hash == target_hash and s1[i - len(s2) + 1:i + 1] == s2:
            return i - len(s2) + 1

    return -1


def spiral_sort(matrix):

    rows,cols = len(matrix) - 1,len(matrix[0]) - 1
    
    values = []
    i = j = 0

    start_row = start_col = 0
    end_row,end_col = rows,cols
    while True:

        

        while j <= end_col:
            values.append(matrix[i][j])
            j += 1

        j -= 1
        i += 1

        while i <= end_row:
            values.append(matrix[i][j])
            i += 1
        
        if start_row == end_row or start_col == end_col:
            break
        i -= 1
        j -= 1

        while j >= start_col:
            values.append(matrix[i][j])
            j -= 1

        j += 1
        i -= 1

        while i > start_row:
            values.append(matrix[i][j])
            i -= 1


        i += 1
        j += 1

        start_row += 1
        start_col += 1

        end_row -= 1
        end_col -= 1

    
    return values 


        


        




def zig_zag(matrix):

    rows,cols = len(matrix) - 1,len(matrix[0]) - 1

    going_up = True

    
    values = []
    i = j = 0

    while 0 <= i <= rows and 0 <= j <= cols:
        
        #if i == rows and j == cols:
        #    values.append(matrix[i][j])
        #    break
        if going_up:
            while i >= 0 and j <= cols:
                values.append(matrix[i][j])
                i -= 1
                j += 1

            if j > cols:
                j -= 1
                i += 2
            elif i < 0:
                i += 1

            going_up = False
        else:
            while i <= rows and j >= 0:
                values.append(matrix[i][j])
                i += 1
                j -= 1


            if i > rows:
                i -= 1
                j += 2
            elif j < 0:
                j += 1
            
            going_up = True
    
    return values


def display(matrix):
    for row in matrix:
        for value in row:
            print(f"{value:<2}",end=' ')

        print()
    print()

if __name__ == "__main__":

    matrix = [[1,2,3,4],
              [14,15,16,5],
              [13,20,17,6],
              [12,19,18,7],
              [11,10,9,8]]
    
    matrix2 = [[2,3,1,6],[12,13,5,7],[8,4,11,9]]
    display(matrix)

    print(spiral_sort(matrix2))



