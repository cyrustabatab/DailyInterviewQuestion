import hashlib


class BloomFilter:

    def __init__(self,a=1000,k=3):
        self.a = [False] * a
        self.hash_algorithms = [hashlib.sha256,hashlib.md5,hashlib.sha1,hashlib.sha384,hashlib.sha512]

        self.hash_functions = [self._get_hash_function(f) for f in self.hash_algorithms[:k]]


    def _get_hash_function(self,f):

        def hash_function(value):

            v = f(str(value).encode('utf-8')).hexdigest()
            return int(v,16) % len(self.a)
        
        return hash_function

    def add(self,value):

        for f in self.hash_functions:
            self.a[f(value)] = True


    def __contains__(self,value):
        return all(f(value) for f in self.hash_functions)




class BIT:

    def __init__(self,nums):
        self.a = [0] * (len(nums) + 1)

        for i,num in enumerate(nums):
            self.update(i + 1,num)


    def update(self,index,num):

        while index < len(self.a):
            self.a[index] += num
            index += index & -index


    def query(self,index):

        total = 0

        while index > 0:
            total += self.a[index]
            index -= index & -index
        
        return total


    def range_query(self,a,b):
        return self.query(b) - self.query(a - 1)


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
