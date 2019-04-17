import time
comparisonCount = 0
assignmentCount = 0
def radix_sort(lst):
    RADIX = 10
    placement = 1
    global comparisonCount
    global assignmentCount

    # get the maximum number
    max_digit = max(lst)


    while placement < max_digit:
      comparisonCount += 1
      # declare and initialize buckets
      buckets = [list() for _ in range( RADIX )]

      # split lst between lists
      for i in lst:
        tmp = int((i / placement) % RADIX)
        buckets[tmp].append(i)
        assignmentCount += 1

      # empty lists into lst array
      a = 0
      for b in range( RADIX ):
        buck = buckets[b]
        assignmentCount += 1
        for i in buck:
          lst[a] = i
          assignmentCount += 1
          a += 1

      # move to next
      placement *= RADIX

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
    radix_sort(unsorted)
    print(unsorted)
    print("Compared: ", comparisonCount, " Assigned: ", assignmentCount)
    end = time.time()
    print(end - start)