# Plan to Implement BST Verifier

1.  **Understand the requirements**:
    *   Implement `is_valid_bst(root)` in `bst_verifier.py`.
    *   A valid BST is defined as:
        *   Left subtree nodes < root node
        *   Right subtree nodes > root node
        *   Both left and right subtrees must be valid BSTs.
2.  **Implementation Details**:
    *   Use a helper function (e.g., `_is_valid_bst_helper(node, min_val, max_val)`) to perform a recursive check.
    *   The `min_val` and `max_val` represent the valid range for the current node's value.
    *   If `node` is `None`, return `True` (an empty tree is a valid BST).
    *   If `node.val` <= `min_val` or `node.val` >= `max_val`, return `False`.
    *   Recursively call the helper on the left subtree with updated `max_val` as `node.val`.
    *   Recursively call the helper on the right subtree with updated `min_val` as `node.val`.
3.  **Testing**:
    *   Write tests in `test_bst_verifier.py` covering various scenarios:
        *   Empty tree
        *   Single node tree
        *   Valid BST
        *   Invalid BST (left node > root)
        *   Invalid BST (right node < root)
        *   Invalid BST (nested invalid node, e.g., root is 5, right child is 8, left child of 8 is 4, which is less than root).
4.  **Execution**:
    *   Update `bst_verifier.py`.
    *   Update `test_bst_verifier.py`.
    *   Run tests using `pytest test_bst_verifier.py` to ensure correctness.
