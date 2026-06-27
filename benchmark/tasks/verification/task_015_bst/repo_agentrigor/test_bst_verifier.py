from bst_verifier import TreeNode, is_valid_bst

def test_valid_bst():
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    assert is_valid_bst(root) == True

def test_invalid_bst():
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)
    assert is_valid_bst(root) == False

def test_empty_tree():
    assert is_valid_bst(None) == True

def test_single_node():
    root = TreeNode(1)
    assert is_valid_bst(root) == True

def test_invalid_nested():
    #   5
    #  / \
    # 4   6
    #    / \
    #   3   7
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(6)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(7)
    assert is_valid_bst(root) == False

if __name__ == "__main__":
    test_valid_bst()
    test_invalid_bst()
    test_empty_tree()
    test_single_node()
    test_invalid_nested()
    print("All tests passed!")
