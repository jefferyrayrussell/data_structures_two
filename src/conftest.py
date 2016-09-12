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
