def preorder(root):
    if not root:
        return

    print(f'v={root.value}, h={root.height}')
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if not root:
        return

    postorder(root.left)
    postorder(root.right)
    print(f'v={root.value} h={root.height}')

def inorder(root):
    if not root:
        return

    inorder(root.left)
    print(f'v={root.value} h={root.height}')
    inorder(root.right)
