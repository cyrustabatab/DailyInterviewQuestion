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
    for i in range(len(s2)):
        letter_to_remove,letter_to_add = s1[i - len(s2)],s1[i]
        current_hash = (current_hash - power * ord(letter_to_remove)) * x + ord(letter_to_add)
        if current_hash == target_hash and s1[i - len(s2) + 1:i + 1] == s2:
            return i - len(s2) + 1

    return -1


def buddy_strings(s1,s2):

    if len(s1) != len(s2):
        return False


    if s1 == s2 and len(s1)  > len(set(s1)): #if string sare the same with duplicate characters
        return True


    differences_s1 = []
    differences_s2 = []
    
    for c1,c2 in zip(s1,s2):
        if c1 != c2:
            differences_s1.append(c1)
            differences_s2.append(c2)

            if len(differences_s1) > 2:
                return False


    if differences_s1[0] != differences_s2[1] or differences_s1[1] != differences_s2[0]:
        return False

    return True




    





