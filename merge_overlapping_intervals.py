





# [(1,3),(2,10),(2,8),(20,25)]
def merge_overlapping_intervals(intervals):

    intervals.sort(key=lambda x: (x[0],x[1]))
    i = 0
    
    result = []
    while i < len(intervals):

        start,end = intervals[i]
        
        max_end = end
        j = i + 1

        while j < len(intervals) and intervals[j][0] < max_end:
            max_end = max(intervals[j][1],max_end)
            j += 1


        result.append((start,max_end))
        i = j

    return result 



        


if __name__ == "__main__":
    

    intervals = [(1,3),(5,8),(4,10),(20,25)]
    intervals_2 = [(1,3),(2,10),(2,8),(20,25)]
    print(merge_overlapping_intervals(intervals_2))




