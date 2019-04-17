from __future__ import print_function
import time


comparisonCount = 0
assignmentCount = 0
def merge_sort(collection):
    """Pure implementation of the merge sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    Examples:
    >>> merge_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> merge_sort([])
    []
    >>> merge_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    global comparisonCount
    global assignmentCount
    length = len(collection)
    if length > 1:
        midpoint = length // 2
        left_half = merge_sort(collection[:midpoint])
        right_half = merge_sort(collection[midpoint:])
        i = 0
        j = 0
        k = 0
        left_length = len(left_half)
        right_length = len(right_half)
        comparisonCount += 1
        while i < left_length and j < right_length:
            comparisonCount += 1
            if left_half[i] < right_half[j]:
                collection[k] = left_half[i]
                assignmentCount += 1
                i += 1
            else:
                collection[k] = right_half[j]
                assignmentCount += 1
                j += 1
            k += 1

        comparisonCount += 1
        while i < left_length:
            collection[k] = left_half[i]
            assignmentCount += 1
            i += 1
            k += 1

        comparisonCount += 1
        while j < right_length:
            collection[k] = right_half[j]
            assignmentCount += 1
            j += 1
            k += 1

    return collection


if __name__ == '__main__':
    try:
        raw_input          # Python 2
    except NameError:
        raw_input = input  # Python 3

    file = open("../inputs/input_1000000.txt","r")

    for line in file:
        l = line

    unsorted = [int(item) for item in l.split(',')]

    start = time.time()
    print(merge_sort(unsorted))
    print("Compared: ", comparisonCount, " Assigned: ", assignmentCount)
    end = time.time()
    print(end - start)

