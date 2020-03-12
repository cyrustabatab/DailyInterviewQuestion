import math

class Number:

    def __init__(self,num):
        self.num = num


    def __lt__(self,number):
        if isinstance(number,Number):

        
            xy = self.num*(10**(math.floor(math.log(number.num,10)) + 1)) + number.num
            yx = number.num*(10**(math.floor(math.log(self.num,10)) + 1)) + self.num

            return xy >= yx




def largest_number_formed_from_array(a):


    print(sorted(a,key=Number))


if __name__ == "__main__":
    
    a = [17, 7, 2, 45, 72]
    print(a)

    largest_number_formed_from_array(a)
