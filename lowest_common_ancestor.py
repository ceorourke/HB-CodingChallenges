class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def lowest_common_ancestor(root, p, q):
    if not root:
        return None
    if (root.data == p) or (root.data == q):
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root
    return left or right

# root = Node(5)
# node2 = Node(9)
# node3 = Node(2)
# node4 = Node(6)
# node5 = Node(3)
# node6 = Node(1)
# node7 = Node(4)
# node8 = Node(10)

# root.left = node2
# root.right = node3
# node2.left = node4
# node2.right = node5
# node3.left = node6
# node3.right = node7
# node5.right = node8

# answer = lowest_common_ancestor(root, 6, 10)
# print answer.data


# another tree
root = Node(12)
node2 = Node(13)
node3 = Node(5)
node4 = Node(17)
node5 = Node(19)
node6 = Node(4)
node7 = Node(6)
node8 = Node(7)

root.left = node2
root.right = node3
node2.left = node4
node2.right = node5
node3.right = node6
node5.left = node7
node5.right = node8

answer = lowest_common_ancestor(root, 7, 17)
print answer.data