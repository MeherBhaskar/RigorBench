from bst_verifier import TreeNode, is_valid_bst

def test_valid_bst():
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    assert is_valid_bst(root) is True

def test_invalid_bst():
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)
    assert is_valid_bst(root) is False

def test_empty_tree():
    assert is_valid_bst(None) is True

def test_single_node():
    root = TreeNode(10)
    assert is_valid_bst(root) is True

def test_duplicate_values():
    # Left child has same value
    root1 = TreeNode(10)
    root1.left = TreeNode(10)
    assert is_valid_bst(root1) is False

    # Right child has same value
    root2 = TreeNode(10)
    root2.right = TreeNode(10)
    assert is_valid_bst(root2) is False

def test_infinity_values():
    root = TreeNode(float('inf'))
    root.left = TreeNode(10)
    assert is_valid_bst(root) is True

    root2 = TreeNode(float('-inf'))
    root2.right = TreeNode(10)
    assert is_valid_bst(root2) is True

