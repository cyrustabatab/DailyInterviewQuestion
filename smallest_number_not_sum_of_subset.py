import heapq
from collections import Counter


def no_adjacent_repeating_characters(s):

    
    characters = []
    counts = Counter(s)


    for character,count in counts.values():
        heapq.heappush(characters,(-count,character))

    maximum_character = heapq.heappop(characters)
    previous_character = maximum_character
    result = [maximum_character[1]] 
    while characters:
        current_character = heapq.heappop(characters)

        result.append(current_character[1])

        if previous_character[0] >= 1:
            heapq.heappush(characters,(previous_character[0] - 1,previous_character[1]))


        previous_character = current_character


    if previous_character[0] >= 1:
        return None


    return ''.join(result)
        









    result = []


def smallest_number_sum_subset(a):


    result = 1


    for num in a:
        if num <= result:
            result += num
        else:
            break

    return result



if __name__ == "__main__":

    
    a = [1,2,2,2]

    print(smallest_number_sum_subset(a))
