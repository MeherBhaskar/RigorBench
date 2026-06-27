import hashlib
from typing import List, Tuple

def verify_merkle_proof(target_hash: str, root_hash: str, proof: List[Tuple[str, str]]) -> bool:
    current_hash = target_hash
    for sibling_hash, direction in proof:
        if direction == 'left':
            combined = sibling_hash + current_hash
        elif direction == 'right':
            combined = current_hash + sibling_hash
        else:
            return False # Invalid direction
        current_hash = hashlib.sha256(combined.encode('utf-8')).hexdigest()
    return current_hash == root_hash
