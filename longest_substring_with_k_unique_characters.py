import pdb
from collections import defaultdict


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


    



# abccdeffg
def longest_substring_with_k_unique_characters(s,k):
    
#    pdb.set_trace()
    i = 0 
    visited = set() 
    
    counts = defaultdict(int)
    longest = float("-inf")
    longest_start = longest_end = None
    current_start = current_end = 0

    while current_end < len(s):
        c = s[current_end]
        counts[c] += 1

        
        if len(counts) == k: 
            if current_end - current_start + 1 > longest:
                longest = current_end - current_start + 1
                longest_start,longest_end = current_start,current_end

        if len(counts) > k:
            counts[s[current_start]] -= 1
            if counts[s[current_start]] == 0:
                del counts[s[current_start]]
            current_start += 1
        current_end += 1
    

    return longest,s[longest_start:longest_end + 1]



if __name__ == "__main__":
   

    s = "aabbcc"
    k = 2

    print(longest_substring_with_k_unique_characters(s,k))


