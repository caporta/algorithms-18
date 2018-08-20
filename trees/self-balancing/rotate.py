def left_rotate(node):
    """
    4
     \                 6
      6     ---->     / \
       \             4   8
        8
    """

    # 1. set tmp to gp's right child
    tmp = node.right
    # 2. set gp's right child to tmp's left child
    node.right = tmp.left
    # 3. set tmp's left child to gp
    tmp.left = node
    # 4. replace gp w/ tmp
    return tmp


def right_rotate(node):
    """
        8
       /               6
      6     ---->     / \
     /               4   8
    4
    """

    # 1. set tmp to gp's left child
    tmp = node.left
    # 2. set gp's left child to tmp's right child
    node.left = tmp.right
    # 3. set tmp's right child to gp
    tmp.right = node
    # 4. replace gp w/ tmp
    return tmp


def right_left_rotate(node):
    """
    4               4
     \               \                 6
      8     ---->     6     ---->     / \
     /                 \             4   8
    6                   8
    """

    # right rotate parent
    node.right = right_rotate(node.right)
    # left rotate gp
    return left_rotate(node)


def left_right_rotate(node):
    """
      8               8
     /               /               6
    4     ---->     6     ---->     / \
     \             /               4   8
      6           4
    """

    # left rotate parent
    node.left = left_rotate(node.left)
    # right rotate gp
    return right_rotate(node)
