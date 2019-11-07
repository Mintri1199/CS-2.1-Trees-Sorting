#!python


def is_sorted(items, start_offset=None, range_end=None):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: O(n) Why and under what conditions?
    TODO: Memory usage: O(1) Why and under what conditions?"""
    if start_offset is None:
        start_offset = 0

    if range_end is None:
        range_end = len(items) - 1

    for i in range(start_offset, range_end):
        if items[i] > items[i + 1]:
            return False

    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Worst Running time: O(n^2) if the array is reverse
    Best Case Running Time: O(n) if the array only has one out of place item
    Memory usage: O(1) Why and under what conditions?"""
    if len(items) <= 1:
        return

    for num_sorted in range(1, len(items)):
        sort = True
        for i in range(len(items) - num_sorted):
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
                sort = False

        if sort:
            break


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Worst Running time: O(n^2)
    Runtime: O(n) if the array only has one out of place item
    Memory usage: O(1) Why and under what conditions?"""
    if len(items) <= 1:
        return

    offset = 0  # Offset the beginning of the array

    while True:
        # Inspired by Zurich
        if offset + 1 == len(items):
            break

        swapped = False
        minimum = items[offset]
        minimum_index = offset
        for i in range(offset, len(items)):
            if items[i] < minimum:
                minimum = items[i]
                minimum_index = i
                swapped = True

        if swapped:
            items[offset], items[minimum_index] = items[minimum_index], items[offset]
        offset += 1


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: O(1) Why and under what conditions?"""
    if len(items) <= 1:
        return

    offset = 0  # Offset the beginning of the array
    sort = False
    while not sort:
        for i in range(offset, -1, -1):
            if items[i] <= items[i + 1]:
                break
            items[i], items[i + 1] = items[i + 1], items[i]

        offset += 1
        sort = is_sorted(items, offset)

# def binary_search(items, target,offset=0):
#     pass
