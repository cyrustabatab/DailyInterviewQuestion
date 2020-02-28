import unittest



def decode_string(s):

    return decode_string_helper(s,0)[0]

def decode_string_helper(s,start):

    result = [] 
    i = start
    while i < len(s):
        c = s[i]
        if c == ']':
            return ''.join(result),i
        if c.isdigit() and s[i +1] == '[':
            r,index = decode_string_helper(s,i + 2)
            result.append(int(c) *r)
            i = index + 1
        else:
            result.append(c)
            i += 1

    return ''.join(result),None



if __name__ == "__main__":


    class Test(unittest.TestCase):

        def setUp(self):
            self.sol = decode_string

        def test_case_1(self):
            s = '2[a2[b]c]' 
            self.assertEqual(self.sol(s),'abbcabbc')

        def test_case_2(self):

            s = 'abc3[4[d]d]'
            self.assertEqual(self.sol(s),'abcddddddddddddddd')


    unittest.main(verbosity=2)
