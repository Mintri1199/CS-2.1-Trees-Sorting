#!python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return repr(self.data)


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ', '.join(nodes) + ']'

    def insert_asc(self, data):
        new_node = Node(data)

        # Case where the linked list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return

        # Case where the insert is prepend
        if data < self.head.data:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return

        current_node = self.head

        # Find the node
        while current_node is not None:
            if data == current_node.data:
                break
            elif current_node.next is not None and current_node.next.data > data:
                break

            current_node = current_node.next

        # Case where the function reach the end of the linked list
        if current_node is None:
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1

        else:
            new_node.next = current_node.next
            current_node.next = new_node
            self.size += 1


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    if len(numbers) == 0:
        return numbers

    min_num = numbers[0]
    max_num = numbers[0]
    # Find the range
    for num in numbers:
        if num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num

    array_size = [0] * (max_num - min_num + 1)
    for num in numbers:
        array_size[num - min_num] += 1

    offset = 0
    for i, occ in enumerate(array_size):
        if occ != 0:
            # mutate the input
            for j in range(occ):
                numbers[j + offset] = i + min_num
            offset += occ


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    min_num = numbers[0]
    max_num = numbers[0]
    # Find the range
    for num in numbers:
        if num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num

    buckets = [LinkedList() for _ in range(num_buckets)]
    divider = (max_num + 1) // num_buckets
    for num in numbers:
        bucket = buckets[num // divider]
        bucket.insert_asc(num)

    pointer = 0

    for bucket in buckets:
        current_node = bucket.head

        while current_node is not None:
            numbers[pointer] = current_node.data
            current_node = current_node.next
            pointer += 1
