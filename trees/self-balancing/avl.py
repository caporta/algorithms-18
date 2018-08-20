class TreeNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 0

class AVLTree():
    def insert(self, root, key):
        if not root:
            return TreeNode(key)
        elif key < root.value:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = self._recalculate_height(root)
        balance = self._get_balance_factor(root)

        if balance > 1 and key < root.left.value:
            print(f'right on v={root.value}')
            return self._right_rotate(root)

        if balance < -1 and key > root.right.value:
            print(f'left on v={root.value}')
            return self._left_rotate(root)

        if balance > 1 and key > root.left.value:
            print(f'left-right on v={root.value}')
            return self._left_right_rotate(root)

        if balance < -1 and key < root.right.value:
            print(f'right-left on v={root.value}')
            return self._right_left_rotate(root)

        return root

    def _get_balance_factor(self, node):
        return self._get_height(node.left) - self._get_height(node.right)

    def _recalculate_height(self, node):
        return 1 + max(self._get_height(node.left), self._get_height(node.right))

    def _get_height(self, node):
        if not node:
            return -1
        return node.height

    def _left_rotate(self, node):
        tmp = node.right
        node.right = tmp.left
        tmp.left = node

        node.height = self._recalculate_height(node)
        tmp.height = self._recalculate_height(tmp)

        return tmp

    def _right_rotate(self, node):
        tmp = node.left
        node.left = tmp.right
        tmp.right = node

        node.height = self._recalculate_height(node)
        tmp.height = self._recalculate_height(tmp)

        return tmp

    def _right_left_rotate(self, node):
        node.right = self._right_rotate(node.right)
        return self._left_rotate(node)

    def _left_right_rotate(self, node):
        node.left = self._left_rotate(node.left)
        return self._right_rotate(node)
