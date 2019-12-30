

def binary_search(a,target,low,high):


    while low <= high:
        mid = (low + high) // 2

        if a[mid] == target:
            return mid

        if target < a[mid]:
            high = mid  - 1
        else:
            low = mid + 1

    return -1

def two_sum_2(a,n):


    a.sort()

    two_pairs = []
    for i in range(1,len(a)):
        num = a[i]
        index = binary_search(a,n - num,0,i -1)
    
        if index != -1 and index != i:
            two_pairs.append((n - num,num))


    return two_pairs

def two_sum(a,n):


    seen = set()
    
    pairs = []
    for num in a:
        target = n - num

        if target in seen:
            pairs.append((target,num))

        seen.add(num)

    return pairs



def longest_increasing_sequence(s):

    assert s
    visited = set()
    
    current_start = 0
    longest = float("-inf")
    longest_start = longest_end = None
    visited.add(s[0])
    for i in range(1,len(s)):
        c = s[i]     
        visited.add(c)
        while visited and len(visited) != i -  current_start + 1:
            visited.remove(s[current_start])
            current_start += 1
        
        visited.add(c)
        if  i - current_start + 1 > longest:
            longest = i - current_start + 1
            longest_start,longest_end = current_start,i
    return s[longest_start:longest_end + 1],longest_end - longest_start + 1

if __name__ == "__main__":
    
    s = 'abrkaabcdefghijjxxx'

    print(longest_increasing_sequence(s))



