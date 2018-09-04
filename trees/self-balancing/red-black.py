class TreeNode():
    RED = 0
    BLACK = 1

    def __init__(self, value, color=RED):
        self.value = value
        self.left = None
        self.right = None
        self.color = color


class RedBlackTree():
    """
    RULES:
    ======

        1) Every node is either RED or BLACK
        2) Root is always BLACK
        3) New insertions are always RED
        4) Every path from root to leaf
        has the same number of BLACK nodes
        5) No path can have two consecutive RED nodes
        6) Nulls are BLACK

    REBALANCING:
    ============

        1) BLACK aunt => rotate (BAR)

                B
               / \
              R   R

        2) RED aunt   => color flip (RAC)

                R
               / \
              B   B

    SAMPLE INSERTS:
    ===============

    3(R) [2 = fix root]

    3(B)

    3(B) -> 1(R)

    3(B) -> 1(R) -> 5(R)

    3(B) -> 1(R) -> 5(R) -> 7(R)* [5 = color flip]

    3(R) -> 1(B) -> 5(B) -> 7(R)* [2 = fix root]

    3(B) -> 1(B) -> 5(B) -> 7(R)

    3(B) -> 1(B) -> 5(B) -> 7(R) -> 6(R)* [5 = rotate]

    3(B) -> 1(B) -> 6(B) -> 5(R) -> 7(R)

    3(B) -> 1(B) -> 6(B) -> 5(R) -> 7(R) -> 8(R)* [5 = color flip]

    3(B) -> 1(B) -> 6(R) -> 5(B) -> 7(B) -> 8(R)

    3(B) -> 1(B) -> 6(R) -> 5(B) -> 7(B) -> 8(R) -> 9(R)* [5 = rotate]

    3(B) -> 1(B) -> 6(R) -> 5(B) -> 8(B) -> 7(R) -> 9(R)

    3(B) -> 1(B) -> 6(R) -> 5(B) -> 8(B) -> 7(R) -> 9(R) -> 10(R)* [5 = color flip]

    3(B) -> 1(B) -> 6(R) -> 5(B) -> 8(R) -> 7(B) -> 9(B) -> 10(R)* [5 = rotate]

    6(B) -> 3(R) -> 1(B) -> 5(B) -> 8(R) -> 7(B) -> 9(B) -> 10(R)

    """

    def insert(self, root, key):
        if not root:
            return TreeNode(key)
        elif key < root.value:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
            if root.color == RED:
                return root
            elif root.right.color == RED:
                if _has_red_child(root.right):
                    return _fix_right(root, key)
                else:
                    return root
            else
                return root

    def _fix_right(self, root, key):
        parent = root.right
        aunt = root.left

        if aunt.color == RED:
            # red aunt, color flip
            root.color = RED
            aunt.color = BLACK
            parent.color = BLACK

            return root

        else:
            # black aunt, rotate
            if key > parent.right.value:
                # left rotate
                tmp = node.right
                node.right = tmp.left
                tmp.left = node
                tmp.color = BLACK
                tmp.left = RED

            if key < parent.right.value:
                # right left rotate
                pass
