import hashlib
import time

def calculate_hash(seed, timestamp):
    # Combine the seed with the timestamp
    input_str = seed + str(timestamp)
    # Compute the SHA-256 hash
    result = hashlib.sha256(input_str.encode()).hexdigest()
    # Return the first 5 characters
    return result[:5]

def find_timestamp_for_hash(seed, start_timestamp):
    # Convert the start timestamp to milliseconds
    timestamp = start_timestamp * 1000
    while True:
        # Calculate the hash
        hash_value = calculate_hash(seed, timestamp)
        # Convert the hash to an integer
        decimal_value = int(hash_value, 16)
        if decimal_value == 0 or decimal_value == 1:
            return timestamp   # Convert back to seconds
        timestamp += 1  # Increase by 1 millisecond

# Example usage
seed = "0"
start_timestamp = int(time.time())  # Current time
result_timestamp = find_timestamp_for_hash(seed, start_timestamp)
print(f"Found timestamp: {result_timestamp} for seed: '{seed}'")
