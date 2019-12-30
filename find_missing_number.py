import unittest


def find_missing_number(a):

    result = 0

    for num in a:
        result ^= num

    return result

def find_missing_and_repeating(a):
    n = len(a) 

    for num in a:
        if a[n -abs(num)] < 0:
            repeating = abs(num)
        else:
            a[n -abs(num)] *= -1


    
    for num in range(1,n + 1):
        if a[n - abs(num)] > 0:
            missing = num


    return repeating,missing

def find_unique_arr(a):

    result_array = [0] * 32

    for num in a:
        for i in range(32):
            result_array[i] += (num >> i) & 1

    result = 0
    for i,bit in enumerate(result_array):
        if bit % 3 != 0:
            result += 2**i

    return result

if __name__ == "__main__":


    class Test(unittest.TestCase):

        def setUp(self):
            self.sol = find_missing_number

        def test_case_1(self):

            a = [4,3,2,4,1,3,2]
            self.assertEqual(self.sol(a),1)


#    unittest.main(verbosity=2)

    a = [1,3,3] 
    print(find_missing_and_repeating(a))


