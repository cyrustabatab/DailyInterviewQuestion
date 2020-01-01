import unittest



def min_steps_to_climb_staircase(n):
    
    steps = (1,2)
    minimum = [[float("inf"),None] for _ in range(n + 1)]
    minimum[0][0] = 1
    minimum[1][0] = 1 #minimum way to get to


    for i in range(1,len(minimum)):
        for step in steps:
            if minimum[i - step][0] + 1 < minimum[i][0]:
                minimum[i][0] = minimum[i - step][0] + 1
                minimum[i][1] = step
    
    
    print(minimum[-1])
    path = reconstruct_steps(minimum)
    print(path)


def reconstruct_steps(minimum):
    path = []
    i = len(minimum) - 1


    while i >= 0:
        path.append(i)
        case = minimum[i][1]
        if case is None:
            break
        i -= case


    return path[::-1]


        










def num_ways_to_climb_stairs(n):

    steps = (1,2) 
    ways = [0] * (n + 1)
    ways[0] = 1 # one way
    ways[1] = 1


    for i in range(2,len(ways)):
        for step in steps:
            ways[i] += ways[i - step]
    

    return ways[-1]




if __name__ == "__main__":
   

    class Test(unittest.TestCase):

        def setUp(self):
            self.sol = num_ways_to_climb_stairs

        def test_case_1(self):
            n = 4
            self.assertEqual(self.sol(n),5)

        def test_case_2(self):
            n = 5
            self.assertEqual(self.sol(n),8)

    

    #unittest.main(verbosity=2)


    n = 5 
    min_steps_to_climb_staircase(n)


