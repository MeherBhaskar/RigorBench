import hashlib
from main import verify_merkle_proof, hash_node

def test_verify_merkle_proof_valid():
    leaf = "hello"
    leaf_hash = hash_node("hello")
    sibling1 = hash_node("world")
    parent_hash = hash_node(leaf_hash + sibling1)
    sibling2 = hash_node("foo")
    root = hash_node(sibling2 + parent_hash)
    proof = [('right', sibling1), ('left', sibling2)]
    assert verify_merkle_proof(leaf, proof, root) == True

def test_verify_merkle_proof_invalid_root():
    leaf = "hello"
    leaf_hash = hash_node("hello")
    sibling1 = hash_node("world")
    parent_hash = hash_node(leaf_hash + sibling1)
    sibling2 = hash_node("foo")
    root = hash_node(sibling2 + parent_hash)
    proof = [('right', sibling1), ('left', sibling2)]
    assert verify_merkle_proof(leaf, proof, "fake_root") == False

def test_verify_merkle_proof_invalid_direction():
    leaf = "hello"
    leaf_hash = hash_node("hello")
    sibling1 = hash_node("world")
    parent_hash = hash_node(sibling1 + leaf_hash)
    root = parent_hash
    proof = [('left', sibling1)]
    assert verify_merkle_proof(leaf, proof, root) == True
    invalid_proof = [('right', sibling1)]
    assert verify_merkle_proof(leaf, invalid_proof, root) == False
