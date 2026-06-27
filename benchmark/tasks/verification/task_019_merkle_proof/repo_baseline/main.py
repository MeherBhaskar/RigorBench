import hashlib

def hash_node(left: str, right: str) -> str:
    """Returns the SHA-256 hash of the concatenated left and right strings."""
    return hashlib.sha256((left + right).encode('utf-8')).hexdigest()

def verify_merkle_proof(root: str, target_leaf: str, proof: list[tuple[str, str]]) -> bool:
    """
    Verifies a Merkle tree proof.
    
    :param root: The expected root hash of the Merkle tree.
    :param target_leaf: The leaf node value to verify (its initial hash).
    :param proof: A list of (direction, sibling_hash) where direction is 'left' or 'right'.
    :return: True if the proof is valid and evaluates to the root, False otherwise.
    """
    current_hash = target_leaf
    for direction, sibling_hash in proof:
        if direction == 'left':
            current_hash = hash_node(sibling_hash, current_hash)
        elif direction == 'right':
            current_hash = hash_node(current_hash, sibling_hash)
        else:
            return False
    return current_hash == root
