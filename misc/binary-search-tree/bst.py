class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None
    
    def add(self, data):
        node = self.root
        if node == None:
            self.root = Node(data)
            return
        else:
            def searchTree(node):
                if data < node.data:
                    if node.left is None:
                        node.left = Node(data)
                        return
                    elif node.left is not None:
                        return searchTree(node.left)
                elif data > node.data:
                    if node.right is None:
                        node.right = Node(data)
                        return
                    elif node.right is not None:
                        return searchTree(node.right)
                else:
                    return None
            return searchTree(node)
    
    def findMin(self):
        current = self.root
        while current.left is not None:
            current = current.left
        return current.data

    def findMax(self):
        current = self.root
        while current.right is not None:
            current = current.right
        return current.data

    def find(self, data):
        current = self.root
        while current.data != data:
            if data < current.data:
                current = current.left
            else:
                current = current.right
        return current.data
    
    def isPresent(self, data):
        current = self.root
        while current:
            if data == current.data:
                return True
            if data < current.data:
                current = current.left
            else:
                current = current.right
            return False
    
    def remove(self, data):
        def removeNode(node, data):
            if node == None:
                return None
            if data == node.data:
                if node.left is None and node.right is None:
                    return None
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left
                tempNode = node.right
                while tempNode.left is not None:
                    tempNode = tempNode.left
                node.data = tempNode.data
                node.right = removeNode(node.right, tempNode.data)
                return node
            elif data < node.data:
                node.left = removeNode(node.left, data)
                return node
            else:
                node.right = removeNode(node.right, data)
                return node

        self.root = removeNode(self.root, data)    

