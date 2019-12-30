from collections import defaultdict,deque


def longest_substring_without_repeating_characters(s):

    
    longest = float("-inf")
    current_start = 0
    max_start = max_end = None
    seen = {s[0]}


    for i in range(1,len(s)):
        c = s[i]
        seen.add(c)
        while i > current_start and len(seen) <  i - current_start + 1:

            seen.remove(s[current_start])
            current_start += 1
        seen.add(c)

        if i - current_start + 1 > longest:
            longest = i - current_start + 1
            max_start,max_end = current_start,i


    return longest
    


    
if __name__ == "__main__":
    

    s = "happiness"
    
    print(longest_substring_without_repeating_characters(s))
