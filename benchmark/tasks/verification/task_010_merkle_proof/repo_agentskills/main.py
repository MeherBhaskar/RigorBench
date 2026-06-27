import hashlib

def hash_node(data: str) -> str:
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def verify_merkle_proof(leaf: str, proof: list, root: str) -> bool:
    """
    Verifies a Merkle tree inclusion proof.
    """
    current_hash = hash_node(leaf)
    for direction, hash_value in proof:
        if direction == 'left':
            current_hash = hash_node(hash_value + current_hash)
        elif direction == 'right':
            current_hash = hash_node(current_hash + hash_value)
        else:
            return False
    return current_hash == root
