import hashlib
from typing import List, Tuple

def verify_merkle_proof(target_hash: str, root_hash: str, proof: List[Tuple[str, str]]) -> bool:
    current_hash = target_hash
    for sibling_hash, direction in proof:
        if direction == 'left':
            L = sibling_hash
            R = current_hash
        elif direction == 'right':
            L = current_hash
            R = sibling_hash
        else:
            return False
            
        combined = L + R
        current_hash = hashlib.sha256(combined.encode('utf-8')).hexdigest()
        
    return current_hash == root_hash
