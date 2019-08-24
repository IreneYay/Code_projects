class Person:
    """ class Person,
    :__init__ instance : first, last, email
    :__str__ instance
    :__eq__ instance: other 
    """
    def __init__(self, first, last, email):
        self.first = first
        self.last = last
        self.email = email
    def __str__(self):
        return '{0} {1} <{2}>'.format(self.first, self.last, self.email)
    def __repr__(self):
        return '({0}, {1}, {2})'.format(self.first, self.last, self.email)
    def __eq__(self, other):
        return self.first == other.first and self.last == other.last and self.email == other.email
        
def order_first_name(a, b):
    """
    Orders two people by their first names
    :param a: a Person
    :param b: a Person
    :return: True if a comes before b alphabetically and False otherwise
    """
    lst_a = a.first
    lst_b = b.first
    #condition to check if first names are equal
    if lst_a < lst_b:
        return True
    if lst_a == lst_b:
        return a.last < b.last
    return a.last > b.last
def order_last_name(a, b):
    """
    Orders two people by their last names
    :param a: a Person
    :param b: a Person
    :return: True if a comes before b alphabetically and False otherwise
    """
    lst_a = a.last
    lst_b = b.last
    if lst_a < lst_b:
        return True
    if lst_a == lst_b:
    #condition to check if last names are equal
        return a.first < b.first
    return a.first > b.first
def is_alphabetized(roster, ordering):
    """
    Checks whether the roster of names is alphabetized in the given order
    :param roster: a list of people
    :param ordering: a function comparing two elements
    :return: True if the roster is alphabetized and False otherwise
    """
    i = 0
    while i < (len(roster)-1):
        x = ((ordering(roster[i], roster[i+1])))
        if roster[i] == roster[i+1]:
            i += 1
            continue
        elif x:
            i += 1
            continue
        return False
    return True
def alphabetize(roster, ordering):
    """
    Alphabetizes the roster according to the given ordering
    :param roster: a list of people
    :param ordering: a function comparing two elements
    :return: a sorted version of roster
    :return: the number of comparisons made
    """
    count = 0
    if len(roster) <= 1:
        return list(roster), 0
    if len(roster) > 1:
        half = len(roster)//2
        left = roster[:half]
        right = roster[half:]
        l_order, l_count = alphabetize(left, ordering)
        count = count + l_count
        r_order, r_count = alphabetize(right, ordering)
        count = count + r_count
        i = 0
        j = 0
        k = 0
        #reference: CSE 331 notes on D2L
        while i < len(l_order) and j < len(r_order):
            if ordering(l_order[i], r_order[j]):
                roster[k] = l_order[i]
                i = i+1
                count += 1
            elif ordering(r_order[j], l_order[i]):
                roster[k] = r_order[j]
                j += 1
                count += 1
            else:
                roster[k] = l_order[i]
                i = i+1
                count += 2
            k = k+1
        while i < len(l_order):
            roster[k] = l_order[i]
            i = i+1
            k = k+1
        while j < len(r_order):
            roster[k] = r_order[j]
            j = j+1
            k = k+1
        return list(roster), count
    return list(roster), 0
