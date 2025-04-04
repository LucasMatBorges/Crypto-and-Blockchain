import hashlib
import time

# Base block data (could represent block header with transactions, timestamp, etc.)
block_base = "example-block-with-transactions"

# Number of zeros the hash must start with (defines the difficulty)
difficulty = 6
target_prefix = "0" * difficulty

# Start nonce and define the maximum (32-bit nonce)
nonce = 0
max_nonce = 2**32

# Print progress every N iterations
log_step = 100_000

print("Mining block...")
print(f"Target: Hash starting with '{target_prefix}'")

# Start measuring total time
start_time = time.time()
step_start_time = start_time  # For tracking time between logs

while nonce < max_nonce:
    # Combine block data + nonce and encode it to bytes
    block_with_nonce = f"{block_base}{nonce}".encode()
    
    # Calculate SHA-256 hash
    hash_result = hashlib.sha256(block_with_nonce).hexdigest()

    # Check if the hash meets the difficulty requirement
    if hash_result.startswith(target_prefix):
        total_time = time.time() - start_time
        print("\n✅ Block successfully mined!")
        print(f"Nonce found: {nonce}")
        print(f"Valid hash: {hash_result}")
        print(f"⏱️ Total time: {total_time:.2f} seconds")
        break

    # Print progress every log_step iterations
    if nonce % log_step == 0:
        now = time.time()
        step_time = now - step_start_time
        total_elapsed = now - start_time
        print(f"Trying nonce: {nonce}... Hash: {hash_result[:16]}... "
              f"Step time: {step_time:.2f}s | Total: {total_elapsed:.2f}s")
        step_start_time = now  # Reset step timer

    nonce += 1

else:
    total_time = time.time() - start_time
    print("❌ No valid hash found within the nonce limit.")
    print(f"⏱️ Total time: {total_time:.2f} seconds")
