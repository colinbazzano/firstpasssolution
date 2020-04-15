# Quick Sort during lecture:


def quicksort(data):
    # base case: if array length 0 or 1 - explicitly defined as sorted, because 1 is sorted and 0 is nothing
    if len(data) < 2:
        return data
    else:
        # pick a pivot might as well pick first because its unsorted, none are better
        pivot = data[0]
        left = []
        right = []
        # put anything smaller into left array
        # put anything bigger into right array
        # do not include pivot - which we have decided is the first value
        for value in data[1:]:
            if value <= pivot:
                left.append(value)
            else:
                right.append(value)
        # return quicksort(left) + pivot + quicksort(right)
        # we put pivot in brackets so we are adding array + array + array, because pivot would otherwise be an int
        return quicksort(left) + [pivot] + quicksort(right)


my_list = [2, 5, 3, 7, 4, 8, 4, 2, 6, 44, 3, 77, 454, 23, 54, 1]

print(quicksort(my_list))

# IN PLACE QUICKSORT!
