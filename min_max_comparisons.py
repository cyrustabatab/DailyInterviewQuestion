


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



class Integer:

    def __init__(self,num):
        self.num = num


    def __lt__(self,integer):
        if isinstance(integer,Integer):

            xy = str(self.num) + str(integer.num)
            yx = str(integer.num) + str(self.num)


            return int(xy) >= int(yx)



def largest_number_formed_from_array(a):


    largest = sorted(a,key=Integer))



# 3 * (n /2) + 1

def min_max_comparisions(a):

    if len(a) % 2 == 1:
        min_value = max_value = a[-1]
    else:
        min_value = max_value = a[0]
    


    for i in range(len(a)//2):
        if nums[2 * i] < nums[2 * i + 1]:
            minimum = nums[2 * i]
            maximum = nums[2 * i + 1]
        else:
            maximum = nums[2 * i]
            minimum = nums[2 * i + 1]



        min_value = min(min_value,minimum)
        max_value = max(max_value,maximum)


    return min_value,max_value




