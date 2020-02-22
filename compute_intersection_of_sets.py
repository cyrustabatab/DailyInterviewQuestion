


def compute_intersection_of_sets(set_1,set_2):
    

    result = []
    seen = set()
    for num in set_1:
        if num not in seen:
        seen.add(num)


    for num in set_2:
        if num not in seen:
            seen.add(num)


    return list(seen)



