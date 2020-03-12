from collections import Counter
import heapq




def rearrangeString(s):


    frequencies = Counter(s)


    heap = []


    for character,frequency in frequencies.items():
        heapq.heappush(heap,(-frequency,character))


    
    previous_character = heapq.heappop(heap)
    result = [previous_character[1]]


    while heap:

        current_character = heapq.heappop(heap)

        result.append(current_character[1])


        if -previous_character[0] > 1:
            heapq.heappush(heap,(previous_character[0] + 1,previous_character[1]))
        

        previous_character = current_character



    if -previous_character[0] > 1:
        return None


    return ''.join(result)




if __name__ == "__main__":
    

    s = "aaabkhdakjhdkafhdakl"

    print(rearrangeString(s))










        







