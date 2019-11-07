from sorting_iterative import bubble_sort, insertion_sort
from random import randint

def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    result_list = []
    items1_index = 0
    items2_index = 0

    while items2_index != len(items2) or items1_index != len(items1):

        if items2[items2_index] <= items1[items1_index]:
            result_list.append(items2[items2_index])
            items2_index += 1
        else:
            result_list.append(items1[items1_index])
            items1_index += 1

        if items2_index == len(items2):
            for i in range(items1_index, len(items1)):
                result_list.append(items1[i])
            return result_list

        elif items1_index == len(items1):
            for i in range(items2_index, len(items2)):
                result_list.append(items2[i])

            return result_list


def in_place_merge(items, lowest_range, highest_range):
    left_index = lowest_range[0]
    right_index = highest_range[0]

    for i in range(lowest_range[0], highest_range[1] - 1):
        # if either indices reach the end of their range

        if items[right_index - 1] < items[left_index]:
            items[right_index - 1], items[left_index] = items[left_index], items[right_index - 1]
            left_index += 1

        elif items[left_index] <= items[right_index]:
            left_index += 1
        else:
            items[right_index], items[left_index] = items[left_index], items[right_index]
            left_index += 1
            right_index += 1


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    middle_index = len(items) // 2
    right_half = items[middle_index:]
    insertion_sort(right_half)
    left_half = items[:middle_index]
    insertion_sort(left_half)

    for index, item in enumerate(merge(right_half, left_half)):
        items[index] = item


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    if len(items) <= 3:
        bubble_sort(items)
    else:
        middle_index = len(items) // 2
        right_half = items[middle_index:]
        merge_sort(right_half)
        left_half = items[:middle_index]
        merge_sort(left_half)

        for index, item in enumerate(merge(right_half, left_half)):
            items[index] = item


def first_partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: Use the low as the pivot) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    pivot_item = items[low]
    swapped_index = low + 1

    for i in range(low + 1, high):
        if items[i] < pivot_item:
            items[i], items[swapped_index] = items[swapped_index], items[i]
            swapped_index += 1

    items[low], items[swapped_index - 1] = items[swapped_index - 1], items[low]

    return swapped_index - 1


def last_partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: Use the low as the pivot) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    pivot_item = items[high]
    swapped_index = low

    for i in range(low, high - 1):
        if items[i] < pivot_item:
            items[i], items[swapped_index] = items[swapped_index], items[i]
            swapped_index += 1

    items[low], items[swapped_index - 1] = items[swapped_index - 1], items[low]

    return swapped_index - 1


def middle_partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: Use the low as the pivot) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`."""
    middle_index = (low + high) // 2
    
    pivot_item = items[middle_index]
    swapped_index = low + 1

    for i in range(low + 1, high):
        if items[i] < pivot_item:
            items[i], items[swapped_index] = items[swapped_index], items[i]
            swapped_index += 1

    items[low], items[swapped_index - 1] = items[swapped_index - 1], items[low]

    return swapped_index - 1


def random_partition(items, low, high):
    random_pivot_index = randint(low, high - 1)
    pivot_item = items[random_pivot_index]
    swapped_index = low + 1

    # swapped initially
    items[low], items[random_pivot_index] = items[random_pivot_index], items[low]

    for i in range(low + 1, high):
        if items[i] < pivot_item:
            items[i], items[swapped_index] = items[swapped_index], items[i]
            swapped_index += 1

    items[low], items[swapped_index - 1] = items[swapped_index - 1], items[low]

    return swapped_index - 1


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?"""

    if low is None and high is None:
        low = 0
        high = len(items)

    if (high - low) < 2:
        return

    pivot_index = random_partition(items, low, high)
    quick_sort(items, pivot_index + 1, high)
    quick_sort(items, low, pivot_index)


if __name__ == '__main__':
    itemNumbers = [56, 1, 78, 12, 45, 13, 84, 11]
    # merge_sort(itemNumbers)
    # print(itemNumbers)

    merge_sort(itemNumbers)
    print(itemNumbers)
