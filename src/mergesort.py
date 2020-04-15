# Merge Sort as followed in Lecture:

# ***UNDERSTAND***
"""merge sort

1. split the list in half
2. split again, and again. Continue the process until we are working with many 'sorted' lists with len(1)
3.
[8] i
[] k
[6] j
---------- compare and merge, over and over
vvv[8] i
[6 8] k
^^^[6] j

[6 8] i
[ ] k
[4 5] j

vvv[6 8] i
[4 5 6 8] k
^^^[4 5] j

k is the subarray because we are preallocating space
"""


def merge(lstA, lstB):
    elements = len(lstA) + len(lstB)
    merged_lst = [0] * elements
    # put back together here
    # sorting happens here
    a = 0  # cursor for list a
    b = 0  # cursor for list b

    for k in range(0, elements):
        # k is our cursor for the sub array
        # compare a and b
        # if a is out of range, push b and iterate
        if a >= len(lstA):  # we're done with a, push remainder of b
            merged_lst[k] = lstB[b]
            b += 1
        # if b is out of range, push b and iterate
        elif b >= len(lstB):  # we're done with b, push remainder of a
            merged_lst[k] = lstA[a]
            a += 1
        # if a is smaller, put it in array and iterate a & k
        elif lstA[a] < lstB[b]:
            merged_lst[k] = lstA[a]
            a += 1
        # if b is smaller put it in array and iterate b & k
        else:
            merged_lst[k] = lstB[b]
            b += 1

    return merged_lst


def mergesort(lst):
    # split here
    # base condition
    # if array size > 1
    # find the middle of the list
    if len(lst) > 1:
        # # sort stuff in left and put stuff to the left in left
        left = mergesort(lst[: len(lst) // 2])
    # sort stuff in right and put the stuff to the right in right
        right = mergesort(lst[len(lst) // 2:])

        lst = merge(left, right)
    # merge left and right

    return lst


my_list = [8, 6, 5, 4, 45, 23, 63, 84, 24, 1, 333,
           65, 349, 923, 9534, 4782, 39886, 2, 29, 93, 549]

# print(mergesort(my_list))


def merge2(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # initialize pointers to the front of A and B arrays
    a = 0
    b = 0
    # compare the first elements of A and B
    # Copy the smallest to merged_arr
    # I am confused on the if a>=len(arrA) of why we are adding it the way we are.
    for i in range(elements):
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
        if arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        else:
            merged_arr[i] = arrB[b]
            b += 1
    return merged_arr


def merge_sort2(arr):
    # Base Case: if the array is empty or len of 1 return
    if len(arr) <= 1:
        return arr
    # split the arrays into half
    left = arr[:len(arr) // 2]
    right = arr[len(arr) // 2:]
    left = merge_sort2(left)
    right = merge_sort2(right)

    return merge2(left, right)

    # sort each half
    # merge them back together
    # return the array


print(merge_sort2(my_list))
