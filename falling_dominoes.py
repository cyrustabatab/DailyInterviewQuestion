


def falling_dominoes(dominoes):

    forces = [0] * len(dominoes)
    
    
    
    force = 0
    # go left to right to calculate net force
    for i in range(len(dominoes)):
        domino = dominoes[i]
        if domino == 'R':
            force = len(dominoes)
        elif domino == 'L':
            force = 0
        else:
            force = max(force - 1,0)
        forces[i] += force

    
    force = 0
    for i in range(len(dominoes)-1,-1,-1):
        domino = dominoes[i]
        if domino == 'R':
            force = 0
        elif domino == 'L':
            force = len(dominoes)
        else:
            force = max(force -1,0)

        forces[i] -= force


    
    print(forces)

    for i,force in enumerate(forces):
        if force == 0:
            dominoes[i] = '.'
        elif force > 0:
            dominoes[i] = 'R'
        else:
            dominoes[i] = 'L'
    



if __name__ == "__main__":
    
    dominoes = ['.','.','R','.','.','.','L','.','.','R','.']

    print(''.join(dominoes))

    falling_dominoes(dominoes)

    print(''.join(dominoes))






