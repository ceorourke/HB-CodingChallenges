"""Given linked list head node, return head node of new, reversed linked list.

For example:

    >>> ll = Node(1, Node(2, Node(3)))
    >>> reverse_linked_list(ll).as_string()
    '321'
"""


class Node(object):
    """Class in a linked list."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def as_string(self):
        """Represent data for this node and it's successors as a string.

        >>> Node(3).as_string()
        '3'

        >>> Node(3, Node(2, Node(1))).as_string()
        '321'
        """

        out = []
        n = self

        while n:
            out.append(str(n.data))
            n = n.next

        return "".join(out)


def reverse_linked_list(head):
    """Given LL head node, return head node of new, reversed linked list.

    >>> ll = Node(1, Node(2, Node(3)))
    >>> reverse_linked_list(ll).as_string()
    '321'
    """

    new_current = None
    current = head

    while current is not None:
        new_current = Node(current.data, new_current)
        current = current.next

    return new_current

    new_current = None
    current = head

    while current:
        new_current = Node(current.data, new_current)
        current = current.next

    return new_current


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. RIGHT ON!\n"
