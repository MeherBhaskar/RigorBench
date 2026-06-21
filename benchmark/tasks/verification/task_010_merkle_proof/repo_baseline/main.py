import hashlib

def hash_node(data: str) -> str:
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def verify_merkle_proof(leaf: str, proof: list, root: str) -> bool:
    """
    Verifies a Merkle tree inclusion proof.
    """
    pass
