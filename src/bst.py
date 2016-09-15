"""Implementation of Binary Search Tree Class and Methods."""


class Node(object):
    """Implement Node class object."""

    def __init__(self, data):
        """Initialize node."""
        self.data = data
        self.parent = None
        self.lchild = None
        self.rchild = None


class BinarySearchTree(object):
    """Implement Binary Search Tree class object."""

    def __init__(self):
        """Initialize binary search tree."""
        self.root = None
        self._len = 0
        self.ldepth = 0
        self.rdepth = 0

    def size(self):
        """Return size of binary search tree."""
        return self._len

    def insert(self, data):
        """Insert node into binary search tree and track depth."""
        new_node = Node(data)
        counter = 1
        if self.root is None:
            self.root = new_node
            self._len += 1
            self.ldepth += 1
            self.rdepth += 1
        else:
            current_node = self.root
            check = True
            while check is True:
                counter += 1
                if new_node.data < current_node.data:
                    if current_node.lchild:
                        current_node = current_node.lchild
                    else:
                        current_node.lchild = new_node
                        new_node.parent = current_node
                        self._len += 1
                        check = False
                elif new_node.data > current_node.data:
                    if current_node.rchild:
                        current_node = current_node.rchild
                    else:
                        current_node.rchild = new_node
                        new_node.parent = current_node
                        self._len += 1
                        check = False
        if new_node.data < self.root.data:
            if counter > self.ldepth:
                self.ldepth = counter
        else:
            if counter > self.rdepth:
                self.rdepth = counter

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
        return max(self.ldepth, self.rdepth)

    def balance(self):
        """Return balance of bst."""
        return self.ldepth - self.rdepth

if __name__ == '__main__':
    """Demonstrate performance of best and worst case search scenarios."""
