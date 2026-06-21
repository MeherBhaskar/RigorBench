from main import verify_merkle_proof, hash_node

def test_verify_merkle_proof_valid():
    leaf1, leaf2, leaf3, leaf4 = "data1", "data2", "data3", "data4"
    
    h1, h2, h3, h4 = hash_node(leaf1, ""), hash_node(leaf2, ""), hash_node(leaf3, ""), hash_node(leaf4, "")
    h12 = hash_node(h1, h2)
    h34 = hash_node(h3, h4)
    root = hash_node(h12, h34)
    
    # Proof for leaf2: combine with h1 (left) -> h12. combine with h34 (right) -> root
    proof = [('left', h1), ('right', h34)]
    assert verify_merkle_proof(root, h2, proof) == True

def test_verify_merkle_proof_invalid_root():
    h2 = hash_node("data2", "")
    h1 = hash_node("data1", "")
    h34 = hash_node(hash_node("data3", ""), hash_node("data4", ""))
    proof = [('left', h1), ('right', h34)]
    
    assert verify_merkle_proof("fake_root_hash", h2, proof) == False

def test_verify_merkle_proof_invalid_direction():
    leaf1, leaf2, leaf3, leaf4 = "data1", "data2", "data3", "data4"
    h1, h2, h3, h4 = hash_node(leaf1, ""), hash_node(leaf2, ""), hash_node(leaf3, ""), hash_node(leaf4, "")
    h12 = hash_node(h1, h2)
    h34 = hash_node(h3, h4)
    root = hash_node(h12, h34)
    
    # Wrong direction for the first step
    proof = [('right', h1), ('right', h34)]
    assert verify_merkle_proof(root, h2, proof) == False

def test_verify_merkle_proof_empty():
    assert verify_merkle_proof("root_hash", "root_hash", []) == True
