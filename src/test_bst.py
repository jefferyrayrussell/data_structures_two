"""Testing for Binary Search Tree."""


def test_insert_on_empty_size():
    """Test size of bst after insert on empty bst."""
    from bst import BinarySearchTree as BST
    test_bst = BST()
    test_bst.insert(10)
    assert test_bst.size() == 1


def test_insert_on_empty():
    """Test data of node after insert on empty bst."""
    from bst import BinarySearchTree as BST
    test_bst = BST()
    test_bst.insert(10)
    assert test_bst._lst[0] == 10


def test_insert_root():
    """Test presence of root on first insertion."""
    from bst import BinarySearchTree as BST
    test_bst = BST()
    test_bst.insert(10)
    assert test_bst.root.data == 10
