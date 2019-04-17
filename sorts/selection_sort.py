from __future__ import print_function
import time

comparisonCount = 0
assignmentCount = 0
def selection_sort(collection):
    """Pure implementation of the selection sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    Examples:
    >>> selection_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> selection_sort([])
    []
    >>> selection_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    global comparisonCount
    global assignmentCount
    length = len(collection)
    for i in range(length - 1):
        least = i
        for k in range(i + 1, length):
            comparisonCount += 1
            if collection[k] < collection[least]:
                least = k
                assignmentCount += 1
        collection[least], collection[i] = (
            collection[i], collection[least]
        )
    return collection


if __name__ == '__main__':
    try:
        raw_input          # Python 2
    except NameError:
        raw_input = input  # Python 3

    file = open("../inputs/input_10000.txt","r")

    for line in file:
        l = line

    unsorted = [int(item) for item in l.split(',')]

    start = time.time()
    print(selection_sort(unsorted))
    print("Compared: ", comparisonCount, " Assigned: ", assignmentCount)
    end = time.time()
    print(end - start)