class TreeSet:
    """
    A set data structure backed by a tree.
    Items will be stored in an order determined by a comparison
    function rather than their natural order.
    """
    def __init__(self, comp):
        """
        Constructor for the tree set.
        You can perform additional setup steps here
        :param comp: A comparison function over two elements
        """
        self.comp = comp
        #added stuff below
        self.root = TreeNode(None)
        self.size = 0
    def __len__(self):
        """
        Counts the number of elements in the tree
        :return:
        """
        return self.size
    def height(self):
        """
        Finds the height of the tree
        :return:
        """
        return self.t_height(self.root)
    def t_height(self, node):
        """
        Function to calcute height
        """
        if node is None:
            return 0
        elif node is not None:
            return 1 + max(self.t_height(node.left), self.t_height(node.right))
        else:
            return -1
    def insert(self, item):
        """
        Inserts the item into the tree
        :param item:
        :return: If the operation was successful
        """
        if self.is_empty():
            self.root = TreeNode(item)
            self.size = self.size+1
            return True
        return self.t_insert(self.root, item)
    def t_insert(self, node, item):
        """
        insert function Helper
        """
        new_node = TreeNode(item)
        if self.comp(item, node.data) < 0:
            if node.left is None:
                self.size = self.size + 1
                self.height = self.t_height(node)+1
                node.left = new_node
                new_node.parent = node
                return True
            else:
                return self.t_insert(node.left, item)
        elif self.comp(item, node.data) > 0:
            if node.right is None:
                self.size = self.size + 1
                self.height = self.t_height(node)+1
                node.right = new_node
                new_node.parent = node
                return True
            else:
                return self.t_insert(node.right, item)
        elif self.comp(item, node.data) == 0:
            return False
    def remove(self, item):
        """
    Removes the item from the tree
    :param item:
    :return: If the operation was successful
        """
        return self.t_remove(self.root, item)
    def t_remove(self, root, item):
        if self.root != None:
            if self.root.data == item:
                if not self.root.left.root and not self.root.right.root:
                    self.root = None
            # If the item to be removed is smaller than the root's value
                elif not self.root.left.root:
                    self.root = self.root.right.root
                elif not self.root.right.root:
                    self.node = self.node.left.node
            if item < self.root.data:
                self.root.left = self.t_remove(self.root.left, item)
                self.height = self.t_height(self.root.left) -1
                return True
            # If the item to be removed is greater than the root's value
            elif item > self.root.data:
                self.root.right = self.t_remove(self.root.right, item)
                self.height = self.t_height(self.root.right) -1
                return True
            else:
                # Node with only one child or no child
                if self.root.left is None:
                    temp = self.root.right
                    self.root = None
                    return True
                elif self.root.right is None:
                    temp = self.root.left
                    self.root = None
                    return True
                #Node with two children(smallest in the right subtree)
                temp = first(self.root.right)
                self.root.data = temp
                self.root.right = self.t_remove(self.root.right, item)
                self.height = self.t_height(self.root.right) -1
                return True
    def __contains__(self, item):
        """
    Checks if the item is in the tree
    :param item:
    :return: if the item was in the tree
        """
        return self.t_contains(self.root, item)
    def t_contains(self, element, item):
        if element is None or element.data is None:
            return False
        if self.comp(item, element.data) == 0:
            return True
        if self.comp(item, element.data) < 0:
            return self.t_contains(element.left, item)
        else:
            return self.t_contains(element.right, item)
    def first(self):
        """
        Finds the minimum item of the tree
        :return:
        """
        if self.is_empty():
            raise KeyError
        min_node = self.root
        while min_node.left:
            min_node = min_node.left
        return min_node.data
    def last(self):
        """
        Finds the maximum item of the tree
        :return:
        """
        if self.is_empty():
            raise KeyError
        min_node = self.root
        while min_node.right:
            min_node = min_node.right
        return min_node.data
    def clear(self):
        """
        Empties the tree
        :return:
        """
        self.root = None
        self.size = 0
    def __iter__(self):
        """
        Does an in-order traversal of the tree
        :return:
        """
        return self.t_iterate(self.root)
    def t_iterate(self, node):
        t_list = []
        if node is not None and node.data is not None:
            if node.left:
                t_list += self.t_iterate(node.left)
            t_list.append(node.data)
            if node.right:
                t_list += self.t_iterate(node.right)
        return iter(t_list)
    def is_disjoint(self, other):
        """
        Check if two TreeSet is disjoint
        :param other: A TreeSet object
        :return: True if the sets have no elements in common
        """
        for item in other:
            if item in self:
                return False
        return True
# Pre-defined methods
    def is_empty(self):
        """
        Determines whether the set is empty
        :return: False if the set contains no items, True otherwise
        """
        return len(self) == 0
    def __repr__(self):
        """
        Creates a string representation of this set using an in-order traversal.
        :return: A string representing this set
        """
        return 'TreeSet([{0}])'.format(','.join(str(item) for item in self))
    def __bool__(self):
        """
        Checks if the tree is non-empty
        :return:
        """
        return not self.is_empty()
    # Helper functions
    # You can add additional functions here
class TreeNode:
    """
    A TreeNode to be used by the TreeSet
    """
    def __init__(self, data):
        """
        Constructor
        You can add additional data as needed
        :param data:
        """
        self.data = data
        self.left = None
        self.right = None
        # added stuff below
        self.parent = None
    def __repr__(self):
        """
        A string representing this node
        :return: A string
        """
        return 'TreeNode({0})'.format(self.data)

