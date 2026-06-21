import hashlib
from main import verify_merkle_proof

def compute_hash(left: str, right: str) -> str:
    return hashlib.sha256((left + right).encode('utf-8')).hexdigest()

def test_verify_merkle_proof_valid():
    leaf1 = hashlib.sha256(b"data1").hexdigest()
    leaf2 = hashlib.sha256(b"data2").hexdigest()
    leaf3 = hashlib.sha256(b"data3").hexdigest()
    leaf4 = hashlib.sha256(b"data4").hexdigest()

    node12 = compute_hash(leaf1, leaf2)
    node34 = compute_hash(leaf3, leaf4)

    root = compute_hash(node12, node34)

    # Proof for leaf1
    proof1 = [('right', leaf2), ('right', node34)]
    assert verify_merkle_proof(root, leaf1, proof1) is True

    # Proof for leaf3
    proof3 = [('right', leaf4), ('left', node12)]
    assert verify_merkle_proof(root, leaf3, proof3) is True

def test_verify_merkle_proof_invalid():
    leaf1 = hashlib.sha256(b"data1").hexdigest()
    leaf2 = hashlib.sha256(b"data2").hexdigest()
    leaf3 = hashlib.sha256(b"data3").hexdigest()
    leaf4 = hashlib.sha256(b"data4").hexdigest()

    node12 = compute_hash(leaf1, leaf2)
    node34 = compute_hash(leaf3, leaf4)

    root = compute_hash(node12, node34)

    # Invalid proof (wrong direction)
    proof_invalid_dir = [('left', leaf2), ('right', node34)]
    assert verify_merkle_proof(root, leaf1, proof_invalid_dir) is False

    # Invalid proof (wrong hash)
    fake_leaf = hashlib.sha256(b"fake").hexdigest()
    proof_invalid_hash = [('right', fake_leaf), ('right', node34)]
    assert verify_merkle_proof(root, leaf1, proof_invalid_hash) is False

def test_verify_merkle_proof_empty():
    leaf1 = hashlib.sha256(b"data1").hexdigest()
    assert verify_merkle_proof(leaf1, leaf1, []) is True
    assert verify_merkle_proof(hashlib.sha256(b"other").hexdigest(), leaf1, []) is False
