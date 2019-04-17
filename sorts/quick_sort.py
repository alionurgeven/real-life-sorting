from __future__ import print_function
import time

comparisonCount = 0
assignmentCount = 0

def quick_sort(ARRAY):
    """Pure implementation of quick sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    Examples:
    >>> quick_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> quick_sort([])
    []
    >>> quick_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    global comparisonCount
    global assignmentCount
    ARRAY_LENGTH = len(ARRAY)
    comparisonCount += 1
    if( ARRAY_LENGTH <= 1):
        return ARRAY
    else:
        PIVOT = ARRAY[0]
        GREATER = [ element for element in ARRAY[1:] if element > PIVOT ]
        LESSER = [ element for element in ARRAY[1:] if element <= PIVOT ]
        assignmentCount += 3
        return quick_sort(LESSER) + [PIVOT] + quick_sort(GREATER)


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
    print(quick_sort(unsorted))
    print("Compared: ", comparisonCount, " Assigned: ", assignmentCount)
    end = time.time()
    print(end - start)