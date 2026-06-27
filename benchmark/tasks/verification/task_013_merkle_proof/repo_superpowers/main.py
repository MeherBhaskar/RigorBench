import hashlib

def verify_merkle_proof(root_hash: str, leaf_hash: str, proof: list) -> bool:
    """
    Verifies a Merkle tree proof.
    """
    current_hash = leaf_hash
    for direction, sibling_hash in proof:
        if direction == 'left':
            combined = sibling_hash + current_hash
        elif direction == 'right':
            combined = current_hash + sibling_hash
        else:
            raise ValueError("Direction must be 'left' or 'right'")
        current_hash = hashlib.sha256(combined.encode('utf-8')).hexdigest()
    
    return current_hash == root_hash
