



def rabin_karp(s1,s2):

    assert len(s1) >= len(s2)

    current_hash = target_hash = 0
    x = 53
    same = True

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




def compare(x,y):

    xy = int(str(x) + str(y))
    yx = int(str(y) + str(x))

    return xy > yx



class Node:


    def __init__(self,num):
        self.num = num


    def __lt__(self,other):
        if isinstance(other,Node):

            xy = int(str(self.num) + str(other.num))
            yx = int(str(other.num) + str(self.num))

            return xy >= yx



def largest_number_formed_from_array(a):


    a = sorted(a,key=Node)
    
    return ''.join(map(str,a))


if __name__ == "__main__":
    

    a = [3,30,34,5,9]

    print(largest_number_formed_from_array(a))
