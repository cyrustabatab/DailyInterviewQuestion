import unittest




def validate_balanced_parentheses(s):
    
    stack = []
    opening = {"(","[","{"} 
    closing_to_opening = {")": "(","]": "[","}": "{"}
    for c in s:
        if c in opening:
            stack.append(c)
        else: # means closing
            value = stack.pop()

            if closing_to_opening[c] != value:
                return False

    
    return not stack


if __name__ == "__main__":
    

    class Test(unittest.TestCase):

        def setUp(self):
            self.sol = validate_balanced_parentheses

        def test_case_1(self):
            s = "((()))"
            self.assertTrue(self.sol(s))

        def test_case_2(self):
            s = "[()]{}"

            self.assertTrue(self.sol(s))

        def test_case_3(self):
            s = "({[)]"
            self.assertFalse(self.sol(s))


    unittest.main(verbosity=2)
