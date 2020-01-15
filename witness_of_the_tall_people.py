import unittest



def witness_of_the_tall_people(heights):

    stack = []
    
    
    witnesses = []
    for height in reversed(heights):

        while stack and height > stack[-1]:
            stack.pop()


        if not stack:
            witnesses.append(height)


        stack.append(height)

    return len(witnesses),witnesses



if __name__ == "__main__":
    
    
    heights = [3,6,3,4,1]


    print(witness_of_the_tall_people(heights))



