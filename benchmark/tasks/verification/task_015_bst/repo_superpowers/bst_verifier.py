class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root: TreeNode) -> bool:
    stack = []
    curr = root
    prev = None
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        if prev is not None and curr.val <= prev:
            return False
        prev = curr.val
        curr = curr.right
    return True

