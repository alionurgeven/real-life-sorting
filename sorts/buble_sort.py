from __future__ import print_function
import time


def bubble_sort(collection):
    """Pure implementation of bubble sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    Examples:
    >>> bubble_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> bubble_sort([])
    []
    >>> bubble_sort([-2, -5, -45])
    [-45, -5, -2]
    
    >>> bubble_sort([-23,0,6,-4,34])
    [-23,-4,0,6,34]
    """
    comparisonCount = 0
    assignmentCount = 0
    length = len(collection)
    for i in range(length-1):
        swapped = False
        for j in range(length-1-i):
            if collection[j] > collection[j+1]:
                comparisonCount += 1
                swapped = True
                collection[j], collection[j+1] = collection[j+1], collection[j]
                assignmentCount += 1
        if not swapped: break  # Stop iteration if the collection is sorted.
        comparisonCount += 1
    print("Compared: ", comparisonCount, " Assigned: ", assignmentCount)
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
    print(*bubble_sort(unsorted), sep=',')
    end = time.time()
    print(end - start)