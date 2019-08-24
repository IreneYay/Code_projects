class Node:
    """ Node class"""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class Deque:
    """A double-ended queue """
    def __init__(self):
        """
        Initializes an empty Deque
        """
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    def __len__(self):
        """
        Computes the number of elements in the Deque
        :return: The size of the Deque
        """
        return self.size
    def peek_front(self):
        """ Looks at, but does not remove, the first element
        :return: The first element
        """
        if self.is_empty():
            raise IndexError
        else:
            first = self.head.next.data
            return first
    def peek_back(self):
        """
        Looks at, but does not remove, the last element
        :return: The last element
        """
        if self.is_empty():
            raise IndexError
        last = self.tail.prev.data
        return last
    def insertAfter(self, old, element):
        """Inserts new node e after old node N, and updates the deque """
        newest = Node(element)
        newest.next = old.next
        newest.prev = old
        old.next = newest
        newest.next.prev = newest
        self.size = self.size + 1
    def push_front(self, e):
        """
        Inserts an element at the front of the Deque
        :param e: An element to insert
        """
        self.insertAfter(self.head, e)
    def push_back(self, e):
        """
        Inserts an element at the back of the Deque
        :param e: An element to insert
        """
        self.insertAfter(self.tail.prev, e)
    def remove(self, item):
        """ Rmoves nodes N and adjust the deque"""
        item.prev.next = item.next
        item.next.prev = item.prev
        self.size = self.size-1
    def pop_front(self):
        """
        Removes and returns the first element
        :return: The (former) first element
        """
        if self.is_empty():
            raise IndexError
        else:
            first = self.head.next.data
            self.remove(self.head.next)
            return first
    def pop_back(self):
        """
        Removes and returns the last element
        :return: The (former) last element
        """
        if self.is_empty():
            raise IndexError
        else:
            last = self.tail.prev.data
            self.remove(self.tail.prev)
            return last
    def clear(self):
        """
        Removes all elements from the Deque
        """
        if self.is_empty():
            return
        element = self.head.next
        while element != self.tail:
            self.remove(element)
            element = element.next
    def __iter__(self):
        """
        Iterates over this Deque from front to back
        :return: An iterator
        """
        current = self.head.next
        while current != self.tail:
            yield current.data
            current = current.next
    def extend(self, other):
        """
        Takes a Deque object and adds each of its elements to the back of self
        :param other: A Deque object
        """
        element = other.head.next
        while element is not other.tail:
            self.push_back(element.data)
            element = element.next
    def drop_between(self, start, end):
        """
        Deletes elements from the Deque that within the range [start, end)
        :param start: indicates the first position of the range
        :param end: indicates the last position of the range(does not drop this element)
        """
        item = self.head.next
        if start < 0:
            raise IndexError
        elif end > self.size:
            raise IndexError
        elif end < start:
            raise IndexError
        for i in range(end):
            if start <= i < end:
                self.remove(item)
            item = item.next
    def count_if(self, criteria):
        """
        counts how many elements of the Deque satisfy the criteri
        :param criteria: a bool function that takes an element of the Deque and returns true if that element matches the criteria and false otherwise
        """
        count = 0
        element = self.head.next
        while element is not self.tail:
            if criteria(element.data):
                count += 1
            element = element.next
        return count
    # provided functions
    def is_empty(self):
        """
        Checks if the Deque is empty
        :return: True if the Deque contains no elements, False otherwise
        """
        return len(self) == 0
    def __repr__(self):
        """
        A string representation of this Deque
        :return: A string
        """
        return 'Deque([{0}])'.format(','.join(str(item) for item in self))
        
