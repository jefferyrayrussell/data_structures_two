"""Module of fixtures for testing."""

import pytest
from bst import BinarySearchTree as BsT


@pytest.fixture()
def bst_one():
    """Create bst with one node."""
    test_bst = BsT()
    test_bst.insert(10)
    return test_bst


@pytest.fixture()
def bst_three():
    """Create bst with three nodes."""
    test_bst = BsT()
    test_bst.insert(10)
    test_bst.insert(7)
    test_bst.insert(15)
    return test_bst


@pytest.fixture()
def unbalanced_performance():
    """Create a worst case unbalanced bst for performance testing."""
    u_bst = BsT()
    u_lst = range(15)
    for i in u_lst:
        u_bst.insert(i)
    return u_bst


@pytest.fixture()
def balanced_performance():
    """Create a best case balanced bst for performance testing."""
    b_bst = BsT()
    b_bst.insert(8)
    b_bst.insert(4)
    b_bst.insert(12)
    b_bst.insert(2)
    b_bst.insert(6)
    b_bst.insert(10)
    b_bst.insert(14)
    b_bst.insert(1)
    b_bst.insert(3)
    b_bst.insert(5)
    b_bst.insert(7)
    b_bst.insert(9)
    b_bst.insert(11)
    b_bst.insert(13)
    b_bst.insert(15)
    return b_bst
