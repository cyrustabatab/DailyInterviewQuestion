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

def longest_substring_with_k_distinct_characters(s,k):

    counts = defaultdict(int)


    current_start = current_end = 0
    longest_start = longest_end = 0
    longest = float("-inf")

    while current_end < len(s):
        c = s[current_end]
        counts[c] += 1

        if len(counts) == k:
            if current_end - current_start + 1 > longest:
                longest = current_end - current_start + 1
                longest_start,longest_end = current_start,current_end
        elif len(counts) > k:

            while len(counts) > k:
                counts[s[current_start]] -= 1
                if counts[s[current_start]] == 0:
                    del counts[s[current_start]]

                current_start += 1


        current_end += 1
    
    return s[longest_start:longest_end + 1],longest

if __name__ == "__main__":
    

    s = "aabcdefff"
    k = 3

    print(longest_substring_with_k_distinct_characters(s,k))






