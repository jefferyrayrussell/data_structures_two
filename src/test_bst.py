"""Module of Testing for Binary Search Tree."""


def test_empty_bst():
    """Test an empty bst class."""
    from bst import BinarySearchTree as BsT
    test_bst = BsT()
    assert test_bst.size() == 0


def test_empty_root():
    """Test root is None on empty bst."""
    from bst import BinarySearchTree as BsT
    test_bst = BsT()
    assert test_bst.root is None


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


def test_contains_on_one(bst_one):
    """Test bst has the item."""
    assert bst_one.contains(10) is True


def test_contains_on_one_fail(bst_one):
    """Test to see a failure."""
    assert bst_one.contains(79) is False


def test_contains_on_three(bst_three):
    """Test bst with 3 nodes contains true."""
    assert bst_three.contains(7)


def test_contains_on_three_right(bst_three):
    """Test bst with 3 nodes right true."""
    assert bst_three.contains(15)


def test_contains_on_three_false(bst_three):
    """Test bst with three nodes returns False."""
    assert bst_three.contains(79) is False


def test_contains_with_more_nodes(bst_three):
    """Test contains with lots of nodes."""
    bst_three.insert(9)
    bst_three.insert(20)
    bst_three.insert(18)
    bst_three.insert(347)
    bst_three.insert(5)
    bst_three.insert(1)
    assert bst_three.contains(18)


def test_contains_with_more_nodes2(bst_three):
    """Test contains with lots of nodes."""
    bst_three.insert(9)
    bst_three.insert(20)
    bst_three.insert(18)
    bst_three.insert(347)
    bst_three.insert(5)
    bst_three.insert(1)
    assert bst_three.contains(1)


def test_contains_with_more_nodes3(bst_three):
    """Test contains with lots of nodes."""
    bst_three.insert(9)
    bst_three.insert(20)
    bst_three.insert(18)
    bst_three.insert(347)
    bst_three.insert(5)
    bst_three.insert(1)
    assert bst_three.contains(347)


def test_contains_with_more_nodes4(bst_three):
    """Test contains with lots of nodes."""
    bst_three.insert(9)
    bst_three.insert(20)
    bst_three.insert(18)
    bst_three.insert(347)
    bst_three.insert(5)
    bst_three.insert(1)
    assert bst_three.contains(79) is False


def test_contains_with_more_nodes5(bst_three):
    """Test contains with lots of nodes."""
    bst_three.insert(9)
    bst_three.insert(20)
    bst_three.insert(18)
    bst_three.insert(347)
    bst_three.insert(5)
    bst_three.insert(1)
    assert bst_three.contains(0) is False


def test_depth_on_empty():
    """Test depth is 0."""
    from bst import BinarySearchTree as BsT
    test_bst = BsT()
    assert test_bst.depth() == 0


def test_depth_on_one(bst_one):
    """Test depth is one on bst of 1."""
    assert bst_one.depth() == 1


def test_depth_on_three(bst_three):
    """Test depth witj three nodes."""
    assert bst_three.depth() == 2


def test_depth_on_4(bst_three):
    """Test depth of 4 nodes."""
    bst_three.insert(20)
    assert bst_three.depth() == 3


def test_depth_of_5_nodes(bst_three):
    """Test depth of 5 nodes."""
    bst_three.insert(20)
    bst_three.insert(18)
    assert bst_three.depth() == 4


def test_depth_of_lefts_and_rights(bst_three):
    """Check depth on bigger bst."""
    bst_three.insert(9)
    bst_three.insert(20)
    bst_three.insert(18)
    bst_three.insert(347)
    bst_three.insert(5)
    bst_three.insert(1)
    assert bst_three.depth() == 4


def test_balance_on_empty():
    """Test balance is 0 on empty."""
    from bst import BinarySearchTree as BsT
    test_bst = BsT()
    assert test_bst.balance() == 0


def test_balance_on_one(bst_one):
    """Test balance is 1 on empty."""
    assert bst_one.balance() == 0


def test_balance_on_three(bst_three):
    """Test balance with three nodes."""
    assert bst_three.balance() == 0


def test_balance_on_four_right(bst_three):
    """Test balance with four nodes heavy right."""
    bst_three.insert(20)
    assert bst_three.balance() == -1


def test_balance_on_five_right(bst_three):
    """Test balance with five nodes heavy right."""
    bst_three.insert(20)
    bst_three.insert(18)
    assert bst_three.balance() == -2


def test_balance_on_four_left(bst_three):
    """Test balance with four nodes heavy left."""
    bst_three.insert(5)
    assert bst_three.balance() == 1


def test_balance_on_five_left(bst_three):
    """Test balance with five nodes heavy left."""
    bst_three.insert(5)
    bst_three.insert(1)
    assert bst_three.balance() == 2
