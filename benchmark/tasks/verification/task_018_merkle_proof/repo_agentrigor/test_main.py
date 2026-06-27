import hashlib
from main import verify_merkle_proof

def compute_hash(data: str) -> str:
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def test_verify_merkle_proof():
    leaf1 = compute_hash("data1")
    leaf2 = compute_hash("data2")
    leaf3 = compute_hash("data3")
    leaf4 = compute_hash("data4")
    
    hash12 = compute_hash(leaf1 + leaf2)
    hash34 = compute_hash(leaf3 + leaf4)
    
    root = compute_hash(hash12 + hash34)
    
    proof1 = [(leaf2, 'right'), (hash34, 'right')]
    assert verify_merkle_proof(leaf1, root, proof1) is True
    
    proof3 = [(leaf4, 'right'), (hash12, 'left')]
    assert verify_merkle_proof(leaf3, root, proof3) is True
    
    invalid_proof1 = [(leaf2, 'left'), (hash34, 'right')]
    assert verify_merkle_proof(leaf1, root, invalid_proof1) is False
    
    invalid_proof2 = [(leaf3, 'right'), (hash34, 'right')]
    assert verify_merkle_proof(leaf1, root, invalid_proof2) is False
    
    assert verify_merkle_proof(root, root, []) is True
    
    assert verify_merkle_proof(leaf1, compute_hash("wrong_root"), proof1) is False

    import pytest
    with pytest.raises(ValueError, match="Invalid direction: up"):
        verify_merkle_proof(leaf1, root, [(leaf2, 'up')])
