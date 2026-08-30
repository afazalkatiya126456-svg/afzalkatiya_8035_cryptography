# Generate SHA-1 hash

import hashlib

text = input("enter message to create hash value:")

SHA1_hash = hashlib.sha1 (text.encode()).hexdigest()

print("SHA-1  Hash:" , SHA1_hash)
