import unittest


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


def longest_palindromic_substring(s):
    
    longest = float("-inf")
    longest_start = longest_end = None

    for i in range(len(s)):
        even_length,even_start,even_end = get_palindrome(s,i -1,i)
        odd_length,odd_start,odd_end = get_palindrome(s,i -1,i + 1,odd=True)


        if even_length > longest:
            longest = even_length
            longest_start,longest_end = even_start,even_end

        if odd_length > longest:
            longest = odd_length
            longest_start,longest_end = odd_start,odd_end
    
    

    return s[longest_start:longest_end + 1]



def get_palindrome(s,i,j,odd=False):
    length = 0

    while i >= 0 and j < len(s) and s[i] == s[j]:
        length += 2
        i -= 1
        j += 1



    return length + 1,i + 1,j -1




    
if __name__ == "__main__":
   
    
    class Test(unittest.TestCase):

        def setUp(self):
            self.sol = longest_palindromic_substring
        
        def test_case_1(self):
            s = "banana"

            self.assertEqual(self.sol(s),"anana")

        def test_case_2(self):
            s = "million"
            self.assertEqual(self.sol(s),"illi")

        def test_case_3(self):

            s = "tracecars"

            self.assertEqual(self.sol(s),"racecar")

    


    unittest.main(verbosity=2)
