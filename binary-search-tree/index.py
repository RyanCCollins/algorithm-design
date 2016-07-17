'''
We begin by examining the root node.
If the tree is null, the key we are searching for
does not exist in the tree. Otherwise, if the key
equals that of the root, the search is successful and
we return the node. If the key is less than that of the
root, we search the left subtree. Similarly, if the
key is greater than that of the root, we search the
right subtree. This process is repeated until the key
is found or the remaining subtree is null. If the searched
key is not found before a null subtree is reached, then the key
is not present in the tree. This is easily expressed as a recursive
algorithm:
'''
def search_recursively(key, node):
    if node is None or node.key == key:
        return node
    elif key < node.key:
        return search_recursively(key, node.left)
    else:
        return search_recursively(key, node.right)

def binary_tree_insert(node, key, value):
    if node is None:
        return NodeTree(None, key, value, None)
    if key == node.key:
        return NodeTree(node.left, key, value, node.right)
    if key < node.key:
        return NodeTree(binary_tree_insert(node.left, key, value), node.key, node.value, node.right)
    else:
        return NodeTree(node.left, node.key, node.value, binary_tree_insert(node.right, key, value))
