class Node(object):
    """A node in a tree"""

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right 

def max_int(root, the_max):
    if not root:
        return the_max
    if root.data > the_max:
        the_max = root.data
    the_max = max_int(root.left, the_max)
    the_max = max_int(root.right, the_max)
    
    return the_max


if __name__ == '__main__':

    root = Node(5)
    second = Node(7)
    third = Node(3)
    fourth = Node(1)
    fifth = Node(10)
    sixth = Node(8)
    seventh = Node(15)

    root.left = second
    root.right = third
    second.left = fourth
    second.right = fifth
    fifth.left = seventh
    third.right = sixth

    answer =  max_int(root, 0)
    print answer
