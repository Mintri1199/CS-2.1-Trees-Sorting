#!python

from binaryheap import BinaryMinHeap


class PriorityQueue(object):
    """PriorityQueue: a partially ordered queue with methods to enqueue items
    in priority order and to access and dequeue its highest priority item.
    Item pairs are stored in a binary min heap for its efficient operations."""

    def __init__(self):
        """Initialize this priority queue."""
        # Initialize new binary min heap to store items in this priority queue
        self.heap = BinaryMinHeap()

    def __repr__(self):
        """Return a string representation of this priority queue."""
        return 'PriorityQueue({} items, front={})'.format(self.size(), self.front())

    def size(self):
        return self.heap.size()

    def is_empty(self):
        """Return True if this priority queue is empty, or False otherwise."""
        return self.heap.is_empty()

    def length(self):
        """Return the number of items in this priority queue."""
        return self.heap.size()

    def enqueue(self, item, priority):
        """Insert the given item into this priority queue in order according to
        the given priority."""
        self.heap.insert((priority, item))

    def front(self):
        """Return the item at the front of this priority queue without removing
        it, or None if this priority queue is empty."""
        if self.heap.is_empty():
            return None

        return self.heap.get_min()[1]

    def dequeue(self):
        """Remove and return the item at the front of this priority queue,
        or raise ValueError if this priority queue is empty."""
        if self.size() == 0:
            raise ValueError('Priority queue is empty and has no front item')

        return self.heap.delete_min()[1]

    def push_pop(self, item, priority):
        """Remove and return the item at the front of this priority queue,
        and insert the given item in order according to the given priority.
        This method is more efficient than calling dequeue and then enqueue."""
        if self.size() == 0:
            raise ValueError('Priority queue is empty and has no front item')

        return self.heap.replace_min((priority, item))[1]


# Tests provided and modified from SWHarrison
def test_priority_queue():

    pri_q = PriorityQueue()
    items = ["Sam", "Suk", "Zurich", "Tom", "Alan", "Betsy", "Eirika", "Kevin", "Ali"]
    priority = 0
    for item in items:
        print("adding ", item, "with priority ", priority)
        pri_q.enqueue(item, priority)
        print(pri_q.heap.items)
        priority = (priority + 1) % 3

    while pri_q.length() > 0:
        print(pri_q.dequeue())

    items = ["Sam", "Suk", "Zurich", "Tom", "Alan", "Betsy", "Eirika", "Kevin", "Ali"]
    priority = 0
    for item in items:
        print("adding",item,"with priority",priority)
        pri_q.enqueue(item, priority)
        priority = (priority + 1)%3

    print(pri_q.push_pop("Jackson", 4))
    print(pri_q.heap.items)

    while pri_q.length() > 0:
        print(pri_q.dequeue())


if __name__ == '__main__':
    test_priority_queue()
