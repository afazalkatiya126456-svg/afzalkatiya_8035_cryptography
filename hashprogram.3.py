# Generate SHA-256 hash

import hashlib

text = input("enter message to create hash value:")

SHA256_hash = hashlib.sha256 (text.encode()).hexdigest()

print("SHA-256  Hash:" , SHA256_hash)
