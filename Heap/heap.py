class Heap:
    """
    A heap-based priority queue
    Items in the queue are ordered according to a comparison function
    """
    def __init__(self, comp):
        """
        Constructor
        :param comp: A comparison function determining the priority of the included elements
        """
        self.comp = comp
        self.heap = []
        self.size = len(self.heap)
#_______________________________________________
    def __len__(self):
        """
        Finds the number of items in the heap
        :return: The size
        """
        return self.size
    def peek(self):
        """
        Finds the item of highest priority
        :return: The item item of highest priority
        """
        if self.is_empty():
            raise IndexError
        else:
            return self.heap[0]
#_________HELPER FUNCTIONS__________________________
    def swap(self, i, j):
        """
        Swaps elements
        """
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    def swap_up(self, i):
        """
        Moves item up the heap according to priority
        """
        heap_parent = (i - 1) // 2
        if i > 0 and self.comp(self.heap[i], self.heap[heap_parent]):
            self.swap(i, heap_parent)
            self.swap_up(heap_parent)
#__________________________________________________________
    def insert(self, item):
        """
        Adds the item to the heap
        :param item: An item to insert
        """
        self.heap.append(item)
        self.size = self.size + 1
        self.swap_up(self.size -1)
#_________HELPER FUNCTIONS_____________________________________
    def swap_down(self, i):
        """
        Moves item down the heap according to priority
        """
        if (2 * i) + 1 < self.size:
            left = (2 * i) + 1
            min_child = left
            if (2 * i) + 2 < self.size:
                if (2 * i) + 2:
                    right = (2 * i) + 2
                if self.comp(self.heap[right], self.heap[left]):
                    min_child = right
                if self.comp(self.heap[min_child], self.heap[i]):
                    self.swap(i, min_child)
                self.swap_down(min_child)
    def heapify(self, i):
        """
        function to compute heapify
        """
        left = (2 * i) + 1
        right = (2 * i) + 2
        small = i
        #print (left, right, self.size)
        if left < self.size and self.comp(self.heap[left], self.heap[i]):
            small = left
        if right < self.size and self.comp(self.heap[right], self.heap[small]):
            small = right

        if small != i:
            self.swap(i, small)
            self.heapify(small)
#_________________________________________________________________
    def extract(self):
        """
        Removes the item of highest priority
        :return: the item of highest priority
        """
        if self.is_empty():
            raise IndexError
        else:
            min_item = self.heap[0]
            self.heap[0] = self.heap[self.size-1]
            self.heap.pop()
            self.size = self.size - 1
        if (self.size > 0):
            self.heapify(0)
        return min_item
    def extend(self, seq):
        """
        Adds all elements from the given sequence to the heap
        :param seq: An iterable sequence
        """
        for item in seq:
            self.insert(item)
    def replace(self, item):
        """
        Adds the item the to the heap and returns the new highest-priority item
        Faster than insert followed by extract.
        :param item: An item to insert
        :return: The item of highest priority
        """
        if self.is_empty():
            return item
        if self.comp(item, self.peek()):
            return item
        root_item = self.heap[0]
        self.heap[0] = item
        self.swap_down(0)
        return root_item
    def clear(self):
        """
        Removes all items from the heap
        """
        self.heap.clear()
        self.size = 0
    def __iter__(self):
        """
        An iterator for this heap
        :return: An iterator
        """
        for item in self.heap:
            yield item
    # Supplied methods
    def __bool__(self):
        """
        Checks if this heap contains items
        :return: True if the heap is non-empty
        """
        return not self.is_empty()
    def is_empty(self):
        """
        Checks if this heap is empty
        :return: True if the heap is empty
        """
        return len(self) == 0
    def __repr__(self):
        """
        A string representation of this heap
        :return:
        """
        return 'Heap([{0}])'.format(','.join(str(item) for item in self))
# Required Non-heap member function
def find_median(seq):
    """
    Finds the median (middle) item of the given sequence.
    Ties are broken arbitrarily.
    :param seq: an iterable sequence
    :return: the median element
    """
    if not seq:
        raise IndexError
    min_heap = Heap(lambda a, b: a < b)
    max_heap = Heap(lambda a, b: a > b)
    for item in seq:
        min_heap.insert(item)
        max_heap.insert(item)
    half = int((len(seq)) / 2)
    for item in range(0, half):
        min_heap.extract()
        max_heap.extract()
    return min_heap.peek()
    
