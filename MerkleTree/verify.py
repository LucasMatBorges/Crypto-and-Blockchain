def verify_proof(proof, node, root, concat):
    data = node
    for item in proof:
        if item['left']:
            data = concat(item['data'], data)
        else:
            data = concat(data, item['data'])
    return data == root
