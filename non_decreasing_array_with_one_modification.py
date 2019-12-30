
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


# a=  [12,16,15,11,8]
def non_decreasing_array_with_one_modification(a):

    if len(a) <= 1:
        return True
    count = 0

    for i in range(0,len(a) - 1):

        if a[i] > a[i +1]:
            if count == 1:
                return False
            #if a middle elementj
            if i - 1 >= 0 and i + 2 < len(a) and a[i] > a[i + 2] and a[i + 1] < a[i -1]:
                return False
            count = 1

    return True






