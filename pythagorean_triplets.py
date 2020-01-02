from collections import Counter
import math



def does_pythagorean_triplet_exist(a:list) -> bool:
    
    
    square_counts = Counter(map(lambda x:x**2,a))
    
    
    triplets = set()
    #case 1: 0,0,0
    if square_counts[0] >= 3:
        return True
    
    #case 2:0,n,n
    if square_counts[0] >= 1:
        for num,count in square_counts.items():
            if count >= 2:
                return True
    

    # case 3: x**2,y**2,z**2
    for i in range(len(a)):
        num_1 = a[i]
        if num_1 == 0:
            continue
        for j in range(i + 1,len(a)):
            num_2 = a[j]
            if num_2 != num_1 and num_2 != 0:
                if num_1**2 + num_2**2 in square_counts:
                    return True

    
    return False






if __name__ == "__main__":
    

    a = [3,5,12,5,13,4,0,0,3]

    print(does_pythagorean_triplet_exist(a))

