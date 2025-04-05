from merkle_tree import MerkleTree
from verify import verify_proof
import hashlib

def simple_hash(left, right):
    return hashlib.sha256((left + right).encode()).hexdigest()

# Initial data
data = ['a', 'b', 'c', 'd']
hashed_leaves = [hashlib.sha256(x.encode()).hexdigest() for x in data]

# Create tree
tree = MerkleTree(hashed_leaves, simple_hash)
root = tree.get_root()
print(f"Merkle Root: {root}")

# Generate proof for the item at position 2 ('c')
index = 2
leaf = hashed_leaves[index]
proof = tree.get_proof(index)
print("Proof:", proof)

# Verify
is_valid = verify_proof(proof, leaf, root, simple_hash)
print("Proof is valid?", is_valid)
