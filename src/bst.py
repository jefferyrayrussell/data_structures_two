"""Implimentation of Binary Search Tree Class and Methods."""


class Node(object):
    """Impliment Node class object."""

    def __init__(self, data):
        """Initialize node."""
        self.data = data
        self.parent = None
        self.lchild = None
        self.rchild = None
        self._depth = 0


class BinarySearchTree(object):
    """Impliment Binary Search Tree class object."""

    def __init__(self):
        """Initialize binary search tree."""
        self.root = None
        self._len = 0

    def size(self):
        """Return size of binary search tree."""
        return self._len

    def insert(self, data):
        """Insert node into binary search tree."""
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            self._len += 1
            self.root._depth = 1
        else:
            current_node = self.root
            check = True
            counter = 1
            while check is True:
                if new_node.data < current_node.data:
                    if current_node.lchild:
                        current_node = current_node.lchild
                        counter += 1
                    else:
                        current_node.lchild = new_node
                        new_node.parent = current_node
                        self._len += 1
                        if current_node.rchild is None:
                            self.root._depth += 1
                        check = False
                elif new_node.data > current_node.data:
                    if current_node.rchild:
                        current_node = current_node.rchild
                        counter += 1
                    else:
                        current_node.rchild = new_node
                        new_node.parent = current_node
                        self._len += 1
                        if current_node.lchild is None:
                            self.root._depth += 1
                        check = False

    def contains(self, data):
        """Check if data is present in bst."""
        check = False
        current_node = self.root
        while check is False:
            if data == current_node.data:
                check = True
            elif data < current_node.data:
                if current_node.lchild:
                    current_node = current_node.lchild
                else:
                    break
            elif data > current_node.data:
                if current_node.rchild:
                    current_node = current_node.rchild
                else:
                    break
        return check

    def depth(self):
        """Return depth of bst."""
        try:
            return self.root._depth
        except AttributeError:
            return 0
