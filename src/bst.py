"""Implimentation of Binary Search Tree Class and Methods."""


class Node(object):
    """Impliment Node class object."""

    def __init__(self, data):
        """Initialize node."""
        self.data = data
        self.parent = None
        self.lchild = None
        self.rchild = None


class BinarySearchTree(object):
    """Impliment Binary Search Tree class object."""

    def __init__(self):
        """Initialize Binary Search Tree."""
        self.root = None
        self._lst = []

    def size(self):
        """Return size of Binary Search Tree."""
        return len(self._lst)

    def insert(self, data):
        """Insert node into binary search tree."""
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            self._lst.append(new_node.data)
        else:
            current_node = self.root
            check = True
            while check is True:
                if new_node.data < current_node.data:
                    if current_node.lchild:
                        current_node = current_node.lchild
                    else:
                        current_node.lchild = new_node
                        new_node.parent = current_node
                        self._lst.append(new_node.data)
                        check = False
                elif new_node.data > current_node.data:
                    if current_node.rchild:
                        current_node = current_node.rchild
                    else:
                        current_node.rchild = new_node
                        new_node.parent = current_node
                        self._lst.append(new_node.data)
                        check = False
