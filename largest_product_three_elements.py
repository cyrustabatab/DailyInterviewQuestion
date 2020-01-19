import unittest



def largest_product_three_elements(a):
    
    assert len(a) >= 3

    a.sort()


    # two cases: largest three or smallest two(negative) with largest
    
    largest_three_product = a[-3] * a[-2] * a[-1]
    smallest_two_with_largest = a[0] * a[1] * a[-1]
    return max(largest_three_product,smallest_two_with_largest)





if __name__ == "__main__":
    

    
    class Test(unittest.TestCase):

        def setUp(self):
            self.sol = largest_product_three_elements
        
        def test_case_1(self):
            a = [-4,-4,2,8]
            self.assertEqual(self.sol(a),128)


        def test_case_2(self):
            a = [-10,-10,-2,-4]
            self.assertEqual(self.sol(a),-80)
        
        def test_case_3(self):
            a = [1,2,3,5,6]
            self.assertEqual(self.sol(a),90)


    unittest.main(verbosity=2)
