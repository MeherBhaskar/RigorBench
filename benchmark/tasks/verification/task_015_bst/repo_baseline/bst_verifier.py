class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root: TreeNode) -> bool:
    def validate(node, low=None, high=None) -> bool:
        if not node:
            return True
        if (low is not None and node.val <= low) or (high is not None and node.val >= high):
            return False
        return (validate(node.left, low, node.val) and
                validate(node.right, node.val, high))

    return validate(root)

