#!/usr/bin/env python3

import traverse
from avl import AVLTree


tree = AVLTree()

root = None
root = tree.insert(root, 10)
root = tree.insert(root, 20)
root = tree.insert(root, 30)
root = tree.insert(root, 40)
root = tree.insert(root, 50)
root = tree.insert(root, 25)

print('=========[preorder]==========')
traverse.preorder(root)
print('=========[postorder]==========')
traverse.postorder(root)
print('=========[inorder]==========')
traverse.inorder(root)
