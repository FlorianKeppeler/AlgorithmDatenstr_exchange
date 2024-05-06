"""
ListElement class that represents a single element
in the list

Copyright 2020, University of Freiburg.

Philipp Schneider <philipp.schneider@cs.uni-freiburg.de>
"""


class ListElement:
    '''
    Class represents element of the list
    '''

    def __init__(self, key=None):
        '''
        Default constructor

        >>> l1 = ListElement()
        >>> l1._key is None
        True
        >>> l1._next is None
        True
        >>> l2 = ListElement(21)
        >>> l2._key
        21
        >>> l2._next is None
        True
        '''
        # The key element of the ListElement
        self._key = key
        # Pointer to the left neighbor of this element
        self._next = None

    def set_next(self, next_element):
        '''
        Set pointer to next list element
        Args:
            ListElement next_element - object to point to

        >>> l1 = ListElement()
        >>> l2 = ListElement()
        >>> l1.set_next(l2)
        >>> l2.set_next(l1)
        >>> l1._next == l2
        True
        >>> l1._next._next == l1
        True
        '''
        self._next = next_element

    def get_next(self):
        '''
        Get the pointer of _next object.
        Returns:
            ListElement: Get the next object

        >>> l1 = ListElement()
        >>> l1.get_next() is None
        True
        >>> l2 = ListElement()
        >>> l1.set_next(l2)
        >>> l2.set_next(l1)
        >>> l1.get_next() == l2
        True
        >>> l1.get_next().get_next() == l1
        True
        '''
        return self._next

    def set_key(self, key):
        '''
        Set key value of current list element
        Args:
            key - key value to set

        >>> e = ListElement()
        >>> e._key is None
        True
        >>> e.set_key(23)
        >>> e._key
        23
        '''
        self._key = key

    def get_key(self):
        '''
        Get key value of current list element
        Returns:
            key value of current list element

        >>> e = ListElement()
        >>> e.get_key() is None
        True
        >>> e.set_key(23)
        >>> e.get_key()
        23
        '''
        return self._key

    def __str__(self):
        '''
        Return string representation of current
        list element
        Returns:
            string of current element

        >>> e = ListElement()
        >>> str(e)
        '[None]'
        >>> e.set_key(42)
        >>> str(e)
        '[42]'
        '''
        return '[{0}]'.format(self._key)
