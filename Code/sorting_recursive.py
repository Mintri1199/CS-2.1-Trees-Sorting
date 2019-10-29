from sorting_iterative import bubble_sort, insertion_sort


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


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: Use the low as the pivot) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p
    pivot_item = items[low]
    swapped_index = low + 1

    for i in range(low + 1, high):
        if items[i] < pivot_item:
            items[i], items[swapped_index] = items[swapped_index], items[i]
            swapped_index += 1

    items[low], items[swapped_index - 1] = items[swapped_index - 1], items[low]

    return swapped_index - 1


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Credit to github.com/SWHarrison for helping me understand this
    if low is None and high is None:
        low = 0
        high = len(items)

    if (high - low) < 2:
        return

    pivot_index = partition(items, low, high)
    quick_sort(items, pivot_index + 1, high)
    quick_sort(items, low, pivot_index)


if __name__ == '__main__':
    itemNumbers = [56, 1, 78, 12, 45, 13, 84, 11, 8, 14, 54, 42, 89, 35, 25, 66, 76]
    # merge_sort(itemNumbers)
    # print(itemNumbers)

    quick_sort(itemNumbers)
    print(itemNumbers)
