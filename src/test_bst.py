"""Module of Testing for Binary Search Tree."""

import pytest


def test_insert_on_empty_size():
    """Test size of bst after insert on empty bst."""
    from bst import BinarySearchTree as BsT
    test_bst = BsT()
    test_bst.insert(10)
    assert test_bst.size() == 1


def test_insert_root():
    """Test presence of root on first insertion."""
    from bst import BinarySearchTree as BsT
    test_bst = BsT()
    test_bst.insert(10)
    assert test_bst.root.data == 10


def test_insert_one_left(bst_one):
    """Test left child insert."""
    bst_one.insert(7)
    assert bst_one.root.lchild.data == 7


def test_insert_one_left_size(bst_one):
    """Test size after left child insert."""
    bst_one.insert(7)
    assert bst_one.size() == 2


def test_insert_one_right(bst_one):
    """Test right child insert."""
    bst_one.insert(15)
    assert bst_one.root.rchild.data == 15


def test_insert_one_right_size(bst_one):
    """Test size after right child insert."""
    bst_one.insert(15)
    assert bst_one.size() == 2


def test_insert_one_left_check_right(bst_one):
    """Test right child after left child insert."""
    bst_one.insert(7)
    assert bst_one.root.rchild is None


def test_insert_one_right_check_left(bst_one):
    """Test left child after right child insert."""
    bst_one.insert(15)
    assert bst_one.root.lchild is None


def test_insert_one_left_check_parent(bst_one):
    """Test parent after left child insert."""
    bst_one.insert(7)
    assert bst_one.root.lchild.parent.data == 10


def test_insert_one_right_check_parent(bst_one):
    """Test parent after right child insert."""
    bst_one.insert(15)
    assert bst_one.root.rchild.parent.data == 10


def test_insert_left_and_right_check_left(bst_one):
    """Test left after both children inserted."""
    bst_one.insert(7)
    bst_one.insert(15)
    assert bst_one.root.lchild.data == 7


def test_insert_left_and_right_check_right(bst_one):
    """Test right after both children inserted."""
    bst_one.insert(7)
    bst_one.insert(15)
    assert bst_one.root.rchild.data == 15


def test_insert_left_and_right_check_size(bst_one):
    """Test size after both children inserted."""
    bst_one.insert(7)
    bst_one.insert(15)
    assert bst_one.size() == 3


def test_insert_data_9(bst_three):
    """Test insert 9 for correct position."""
    bst_three.insert(9)
    assert bst_three.root.lchild.rchild.data == 9


def test_insert_data_20(bst_three):
    """Test insert 20 for correct position."""
    bst_three.insert(20)
    assert bst_three.root.rchild.rchild.data == 20


def test_insert_data_18(bst_three):
    """Test insert 18 for correct position."""
    bst_three.insert(20)
    bst_three.insert(18)
    assert bst_three.root.rchild.rchild.lchild.data == 18
