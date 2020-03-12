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

    power = x**(len(s2) - 1)

    for i in range(len(s2),len(s1)):
        letter_to_remove,letter_to_add = s1[i - len(s2)],s1[i]
        current_hash = (current_hash - power * ord(letter_to_remove)) * x + ord(letter_to_add)
        if current_hash == target_hash and s1[i - len(s2) + 1:i + 1] == s2:
            return i - len(s2) + 1

    return -1


def convert_roman_numeral_to_decimal(roman_numeral):


    mapping = {"I": 1,"V": 5,"X": 10,"C": 100,"L": 50,"D": 500,"M": 1000}


    
    i = 0

    
    number = 0
    while i < len(roman_numeral):
        c = roman_numeral[i]
        value = mapping[c]

        if i + 1 < len(roman_numeral) and mapping[roman_numeral[i +1]] > value:
            number += mapping[roman_numeral[i +1]] - value 
            i += 2
        else:
            number += value
            i += 1


    return number


if __name__ == "__main__":
    

    class Test(unittest.TestCase):

        def setUp(self):
            self.sol = convert_roman_numeral_to_decimal

        def test_case_1(self):
            s = "IX"
            self.assertEqual(self.sol(s),9)

        def test_case_2(self):
            s = "VII"
            self.assertEqual(self.sol(s),7)

        def test_case_3(self):
            s = "MCMIV"
            self.assertEqual(self.sol(s),1904)

    

    unittest.main(verbosity=2)






