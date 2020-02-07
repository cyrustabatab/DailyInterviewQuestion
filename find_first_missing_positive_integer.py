




def find_first_missing_positive_integer(a):


    elements = set(a)

    i = 1

    while True:

        if i not in elements:
            return i

        
        i += 1


def find_first_missing_positive_2(a):

    if not nums: #if emtpy, just return 1
        return 1

    for i,num in enumerate(nums):
        while i + 1 != nums[i] and 0 < num[i] <= len(nums):
            v = nums[i]
            nums[i],nums[v -1] = nums[v -1],nums[i]

            if nums[i] == nums[v -1]:
                break






