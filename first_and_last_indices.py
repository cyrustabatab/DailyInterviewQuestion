import unittest


def find_first_and_last_indices(a,num):
    
    first = find_first_occurence(a,num)
    last = find_last_occurence(a,num)
    
    return first,last


def find_first_occurence(a,num):

    low,high = 0,len(a) - 1

    while low <= high:
        mid = (low + high) // 2

        if a[mid] == num and (mid == 0 or a[mid -1] != num):
            return mid
        
        if a[mid] >= num:
            high = mid - 1
        else:
            low = mid + 1

    return -1 

def find_last_occurence(a,num):
    low,high = 0,len(a) - 1

    while low <= high:
        mid = (low + high) // 2

        if a[mid] == num and (mid == len(a) - 1 or a[mid + 1] != num):
            return mid

        if a[mid] <= num:
            low = mid + 1
        else:
            high = mid - 1

    return -1


if __name__ == "__main__":
    

    class Test(unittest.TestCase):

        def setUp(self):
            self.sol = find_first_and_last_indices

        def test_case_1(self):
            a = [1,3,3,5,7,8,9,9,9,15]
            target = 9
            self.assertEqual(self.sol(a,target),(6,8))

        def test_case_2(self):
            a =[100,150,150,153]
            target = 150
            self.assertEqual(self.sol(a,target),(1,2))

        def test_case_3(self):
            a = [1,2,3,4,5,6,10]
            target = 9
            self.assertEqual(self.sol(a,target),(-1,-1))



    unittest.main(verbosity=2)
