import hashlib

class MerkleTree:
    def __init__(self, leaves, hash_func=None):
        self.leaves = leaves
        self.hash_func = hash_func or self.default_hash

    def default_hash(self, left, right):
        return hashlib.sha256((left + right).encode()).hexdigest()

    def get_root(self, leaves=None):
        if leaves is None:
            leaves = self.leaves
        if len(leaves) == 1:
            return leaves[0]
        layer = []
        for i in range(0, len(leaves), 2):
            left = leaves[i]
            right = leaves[i + 1] if i + 1 < len(leaves) else None
            if right:
                layer.append(self.hash_func(left, right))
            else:
                layer.append(left)
        return self.get_root(layer)

    def get_proof(self, index, layer=None, proof=None):
        if layer is None:
            layer = self.leaves
        if proof is None:
            proof = []

        if len(layer) == 1:
            return proof

        new_layer = []
        for i in range(0, len(layer), 2):
            left = layer[i]
            right = layer[i + 1] if i + 1 < len(layer) else None

            if right:
                new_layer.append(self.hash_func(left, right))

                if i == index or i == index - 1:
                    is_left = index % 2 == 0
                    proof.append({
                        'data': right if is_left else left,
                        'left': not is_left
                    })
            else:
                new_layer.append(left)

        return self.get_proof(index // 2, new_layer, proof)